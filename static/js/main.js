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

$(document).on('click','.success_btn',function(){
    var $this = $(this);
    console.log($this[0]);
    // var taskId = $this.data('taskid');
    var condition = $this.data('condition');
    var card = $this.parents('.card.task-contents');

    // 完了ボタンのクラスの切り替え(見た目の変化)
    $this.stop(true).toggleClass('clicked');

    if(condition == "1"){
        var finTasks = card.parents('.card-body').children('.fin-tasks');
        // 状態変化+完了タスクリストに入れる
        $this[0].dataset.condition = "3";
        card.parent().fadeOut(150,function(){
            $(this).appendTo(finTasks);
            $(this).show();
        });
        // card.parent().appendTo(finTasks);

        // 並び替え
        var sortedFinTasks = sortCard(finTasks.children());
        finTasks.empty();
        sortedFinTasks.each(function(){
            finTasks.append($(this));
        });
        console.log("完了");
    }else if(condition == "3"){
        var newTasks = card.parents('.card-body').children('.new-tasks');
        // 状態変化+新規タスクリストに入れる
        $this[0].dataset.condition = "1";
        card.parent().fadeOut(150,function(){
            $(this).appendTo(newTasks);
            $(this).show();
        });
        // card.parent().appendTo(newTasks);

        // 並び替え
        var sortedNewTasks = sortCard(newTasks.children());
        newTasks.empty();
        sortedNewTasks.each(function(){
            newTasks.append($(this));
        });
        console.log("完了");
    }
});