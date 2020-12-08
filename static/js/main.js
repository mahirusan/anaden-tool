// ドキュメントがリロードされた後に読み込む設定
document.addEventListener('DOMContentLoaded',function(){
    // 初期表示の設定
    $('.menu-content').toggle();
    $('.click-menu').toggle();
    $('.fin-tasks').toggle();


    // メニューボタンのクリックイベント
    $('.menu-btn').click(function(){
        $('.menu-content').stop(true).toggle('fast');
        $('.click-menu').stop(true).animate({'width':'toggle'});
        $('.main-contents').stop(true).toggleClass('click-menu-open');
    });

    // 完了済タスクを見るボタンのクリックイベント
    $('.fintask-btn').click(function(){
        var $this = $(this);
        var pare = $this.parent();
        pare.siblings('.fin-tasks').slideToggle();
    });

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
        var taskId = $this.data('taskid');
        var condition = $this.data('condition');
        var card = $this.parents('.card.task-contents');

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
            $this.stop(true,false).toggleClass('clicked'); // 完了ボタンのクラスの切り替え(見た目の変化)
            $('#story-achieve-rate').text(data[`achievement_rate`]+"%です"); //進捗率のところの変更
            $('#story-achieve-rate-bar').css({
                width:parseInt(data[`achievement_rate`])+'%',
                'text-align':'center',
            }); //進捗率バーも忘れずに更新する
        }).fail(function(msg){
            console.log('Ajax Error');
        }).always(function(){
            //成否にかかわらず実行
            canAjax = true; //再びAjaxが実行できる
        });
    });
});
