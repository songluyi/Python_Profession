/**
 * Created by Administrator on 2016/9/20.
 */

function Change() {
    var left = document.getElementById('header').value;

    var right_dom = document.getElementById('json');

    var right_notice=document.getElementById('notice_back');

    var middle_bottle;
    var middle_branch;
    var middle_little_branch,middle_dirt_branch;

    var new_right_value='';
    if (left.indexOf(":")!==-1) {
//            alert('符合标准');
        middle_bottle=left.split('\n');
        console.log(middle_bottle);
        for (middle_branch in middle_bottle){
            if (middle_bottle.hasOwnProperty(middle_branch)){
                middle_little_branch=middle_bottle[middle_branch].split(':');
                console.log(middle_little_branch);
                for (middle_dirt_branch in middle_little_branch){
                    if (middle_little_branch.hasOwnProperty(middle_dirt_branch)) {
                        console.log(middle_dirt_branch);
                        if (middle_dirt_branch==0){
                            if (middle_little_branch[middle_dirt_branch].indexOf("www")!==-1){
                                new_right_value=new_right_value+':'+middle_little_branch[middle_dirt_branch]+'"';
                                console.log(middle_little_branch[middle_dirt_branch])
                            }else{
                                new_right_value=new_right_value+'"'+middle_little_branch[middle_dirt_branch]+'"'+':'
                            }

                        }
                        if (middle_dirt_branch==1) {
                            if (middle_little_branch[middle_dirt_branch].indexOf('http') !== -1) {
                                console.log(middle_little_branch[middle_dirt_branch]);
                                new_right_value = new_right_value + '"' + middle_little_branch[middle_dirt_branch]
                            } else {
                                new_right_value = new_right_value + '"' + middle_little_branch[middle_dirt_branch] + '"' + ',';
                            }
                        }
                        if (middle_dirt_branch==2){
                                console.log(middle_little_branch[middle_dirt_branch]);
                                new_right_value=new_right_value+middle_little_branch[middle_dirt_branch]+'"'+',';
                            }
                        

                    }

                }
            }


        }
        console.log(new_right_value);
//            new_right_value=new_right_value.
        right_dom.value = '{'+new_right_value.substring(0,new_right_value.length-1)+'}';
//            alert(left)
    }else{
        alert('不符合标准');
        right_dom.value = "fuck you";
    }
//        right_dom.value = left;
//将右侧提示不显示
    right_notice.style='display:none;';
}
