<!--    function randomString(len) {-->
<!--　　len = len || 32;-->
<!--　　var $chars = 'ABCDEFGHJKMNPQRSTWXYZabcdefhijkmnprstwxyz2345678';-->
<!--　　var maxPos = $chars.length;-->
<!--　　var pwd = '';-->
<!--　　for (i = 0; i < len; i++) {-->
<!--　　　　pwd += $chars.charAt(Math.floor(Math.random() * maxPos));-->
<!--　　}-->
<!--　　return pwd;-->
<!--}-->
       function deleteTr(obj){
           obj.parentNode.parentNode.remove();
           }
        var j=1;
        function addtr(){
            var tableobj =document.getElementById("tid");
            var vlist=["User2","LOS","5105105105105100", "(319)-883-4480", "2020-02-23","7f38e7a645fbd1b3c68fbc75ecd62d24"]
            var trobj =document.createElement("tr");
            <!--Generate new line with data from vlist-->
            for (var i = 0; i < vlist.length; i++) {
                suffix=Math.floor(Math.random()*100000)
                var tdobj = document.createElement("td");
                if (i==0){
                    tdobj.innerHTML="User"+suffix;
                } else if (i==4){
                    var d=new Date()
                    tdobj.innerHTML=d.toUTCString()
                } else {
                    tdobj.innerHTML=vlist[i];
                    }
                trobj.appendChild(tdobj);
            }
            var tdobj = document.createElement("td");
            tdobj.innerHTML="<input type='button' value='Book' onclick='deleteTr(this)'>";
            trobj.appendChild(tdobj);
            tableobj.appendChild(trobj);
        }