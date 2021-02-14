// ドキュメントがリロードされた後に読み込む設定
document.addEventListener('DOMContentLoaded',function(){
    // 初期表示の設定
    $('.menu-content').toggle();
    $('.click-menu').toggle();
    // $('.fin-tasks').toggle();
});
function sortCard(cards){
    var sortedCards = cards.sort(function(a,b){
        // console.log($(a).data('num'));
        // a,bのカスタムデータを取得
        var aNum = $(a).data('num');
        var bNum = $(b).data('num');

        // 昇順ソート(不等号を逆にすれば降順にもできる)
        if(Number(aNum) > Number(bNum)){
            return 1;
        }else if(Number(aNum) < Number(bNum)){
            return -1;
        }
        return 0;
    });
    // console.log(sortedCard);
    return sortedCards;
}



$(function(){

    var canAjax = true;

    //ドキュメント全体のsuccess_btnクラスにクリックイベントを追加
    $(document).on('click','.success_btn',function(){
        //Ajax処理中は新たな処理をスタートしない
        if(!canAjax){
            console.log('通信中');
            return;
        }
        canAjax = false; //新たなAjaxが発生しないようにフラグを切り替えておく

        var $this = $(this);
        // console.log($this[0]); //[DEBUG]
        var taskId = $this.data('taskid');
        var condition = $this.data('condition');
        var card = $this.parents('.card.task-contents');

        // 完了ボタンのクラスの切り替え(見た目の変化)
        // $this.stop(true).toggleClass('clicked');


        $.ajax({
            type:"get",
            url:"/subtask_update/",
            dataType:"json",
            data:{
                "task_id":taskId,
                "condition":condition
            }
        })
        .done(function(data){
            console.log('Ajax Success'); //[DEBUG]
            $this.stop(true).toggleClass('clicked');

            if(condition == "1"){
                var finTasks = card.parents('.card-body').children('.fin-tasks');
                // 状態変化+完了タスクリストに入れる
                $this[0].dataset.condition = "3";
                card.parent().fadeOut(150,function(){
                    $(this).appendTo(finTasks);
                    $(this).show();
                
                    //以下の処理をfadeOut外に持っていくとfinTasksに
                    //要素が移動しきらず次の処理に行くので中に入れました
                    var sortedFinTasks = sortCard(finTasks.children()); // 並び替え
                    finTasks.empty();
                    sortedFinTasks.each(function(){
                        finTasks.append($(this));
                    });
                console.log("完了");
                }); 
            }else if(condition == "3"){
                var newTasks = card.parents('.card-body').children('.new-tasks');
                // 状態変化+新規タスクリストに入れる
                $this[0].dataset.condition = "1";
                card.parent().fadeOut(150,function(){
                    $(this).appendTo(newTasks);
                    $(this).show();
                
                    //以下の処理をfadeOut外に持っていくとfinTasksに
                    //要素が移動しきらず次の処理に行くので中に入れました
                    var sortedNewTasks = sortCard(newTasks.children()); // 並び替え
                    newTasks.empty();
                    sortedNewTasks.each(function(){
                        newTasks.append($(this));
                    });
                    console.log("完了");
                });
            }
            // if(condition == "1"){
        //     $this.data('condition',"3");
            //     card.parent().appendTo(finTasks);
            //     // card.siblings('.card-space').appendTo(finTasks);
            //     // 移動したタスクの並び替え
            //     // console.log(finTasks.children());//[DEBUG]
            //     var sortedFinTasks = sortCard(finTasks.children());
            //     console.log(sortedFinTasks);
            //     // console.log(finTasks.children()); //[DEBUG]
            //     finTasks.empty();
            //     sortedFinTasks.each(function(){
            //         finTasks.append($(this));
            //     });
            // }else if(condition == "3"){
            //     $this.data('condition',"1");
            //     card.parent().appendTo(newTasks);
            //     // card.siblings('.card-space').appendTo(newTasks);
            //     // 移動したタスクの並び替え
            //     // console.log(newTasks.children()); //[DEBUG]
            //     var sortedNewTasks = sortCard(newTasks.children());
            //     console.log(sortedNewTasks); //[DEBUG]
            //     newTasks.empty();
            //     sortedNewTasks.each(function(){
            //         newTasks.append($(this));
            //     });
            // }
            // card.slideToggle('fast');
        }).fail(function(msg){
            console.log('Ajax Error');
            // console.log(taskId);
            // console.log(condition);
        }).always(function(){
            //成否にかかわらず実行
            canAjax = true; //再びAjaxが実行できる
        });

        // if(condition == "1"){
        //     var finTasks = card.parents('.card-body').children('.fin-tasks');
        //     // 状態変化+完了タスクリストに入れる
        //     $this[0].dataset.condition = "3";
        //     card.parent().fadeOut('fast').queue(function(){
        //         $(this).appendTo(finTasks);
        //         $(this).show();

        //         //以下の処理をfadeOut外に持っていくとfinTasksに
        //         //要素が移動しきらず次の処理に行くので中に入れました
        //         var sortedFinTasks = sortCard(finTasks.children()); // 並び替え
        //         finTasks.empty();
        //         sortedFinTasks.each(function(){
        //             finTasks.append($(this));
        //         });
        //         console.log("完了");
        //     }); 
        // }else if(condition == "3"){
        //     var newTasks = card.parents('.card-body').children('.new-tasks');
        //     // 状態変化+新規タスクリストに入れる
        //     $this[0].dataset.condition = "1";
        //     card.parent().fadeOut(150,function(){
        //         $(this).appendTo(newTasks);
        //         $(this).show();

        //         //以下の処理をfadeOut外に持っていくとfinTasksに
        //         //要素が移動しきらず次の処理に行くので中に入れました
        //         var sortedNewTasks = sortCard(newTasks.children()); // 並び替え
        //         newTasks.empty();
        //         sortedNewTasks.each(function(){
        //             newTasks.append($(this));
        //         });
        //         console.log("完了");
        //     });
        // }
    });
});