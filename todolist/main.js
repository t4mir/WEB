
function btnClick() {    
        var text=document.getElementById("to3").value;  
        document.getElementById("to3").value="";
        if(text.length==0) {
            alert("Error 404");
        }
        else if(text.length>0) {
            var list =document.getElementById("list");
            var any_task=document.createElement("div");
            list.appendChild(any_task);
            any_task.className="any_task";
            var checkbox = document.createElement("input");
            checkbox.className="checkbox";
            any_task.appendChild(checkbox);
            checkbox.type="checkbox";
            checkbox.onclick=function toLine() {
                var partoLine=this.parentElement.getElementsByClassName("tasks")[0];
                if(this.checked) {
                    partoLine.style.textDecoration="line-through"
                }
                else {
                    partoLine.style.textDecoration="none";
                }
            }
            var paragraphDiv = document.createElement("div");
            paragraphDiv.className = "tasks";
            var paragraph = document.createElement("p");
            var newP = document.createTextNode(text);
            any_task.appendChild(paragraphDiv);
            paragraphDiv.appendChild(paragraph);
            paragraph.appendChild(newP);


            var deleteDiv = document.createElement("div");
            var del = document.createElement("button");
            del.className = "del";
            del.innerHTML = "delete";
            any_task.appendChild(deleteDiv);
            deleteDiv.appendChild(del);
            del.onclick = function toDel(){
                this.parentElement.parentElement.remove();
            }
        }
    }
