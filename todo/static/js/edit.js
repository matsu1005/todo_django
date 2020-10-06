function editFunction(ele) {
  var task_id = ele.id;
  const div = document.getElementById("form_box_" + task_id);
  const task_name = document.getElementById("task_" + task_id).innerText;
  if (!div.hasChildNodes()){
    const div2 = document.createElement("div");
    const input_task = document.createElement("input");
    input_task.setAttribute("value",task_name);
    input_task.setAttribute("name", "task");
    input_task.setAttribute("type", "text");
    input_task.setAttribute("class", "form-control");
    div2.setAttribute("class", "col");
    
    const input_target = document.createElement("input");
    const div3 = document.createElement("div");
    input_target.setAttribute("type", "datetime-local");
    input_target.setAttribute("name", "target");
    input_target.setAttribute("class", "form-control");
    input_target.setAttribute("style", "width: 70%;");
    div3.setAttribute("class", "col");

    const submit = document.createElement("input");
    submit.setAttribute("type", "submit");
    submit.setAttribute("value", "反映");
    submit.setAttribute("class", "btn btn-info");

    div2.appendChild(input_task);
    div.appendChild(div2);
    div3.appendChild(input_target);
    div.appendChild(div3);
    div.appendChild(submit);

    ele.innerText = "閉じる"
  } else {
    ele.innerText = "編集"
    while (div) div.removeChild(div.firstChild);
  }
}