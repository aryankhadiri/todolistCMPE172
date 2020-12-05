
var currentDate = $(".date-input").val();
var totalForms = document.getElementById("id_form-TOTAL_FORMS").value;

function disableSave(){
    if ($(".date-input").val() != currentDate){
        $("#save-button").attr("disabled", true);
    }
    else{
        $("#save-button").attr("disabled", false);

    }
}
jQuery(function(){
    $(".delete-task-button").on("click", function(){
        $(this).parent('div').parent('div').remove();
    })
    $("#add-task-button").on("click", function(){
        //console.log(totalForms)
        var taskDesc = document.getElementById("task-description-field");
        var taskDone = document.getElementById("task-done-box");
        //console.log(taskDone);
        var newTaskDesc = taskDesc.cloneNode(true)
        var newTaskDone = taskDone.cloneNode(true)
        newTaskDesc.name = "form-"+totalForms+"-task"
        newTaskDone.name = "form-"+totalForms+"-done"
        totalForms = parseInt(totalForms) + 1;
        document.getElementById("id_form-TOTAL_FORMS").value = totalForms.toString();
        $(".newTasks").append("<div class = 'newTask'></div>");
        $(".newTask").each(function(){
            if ($(this).length == 1){
                $(this).append(newTaskDesc);
                $(this).append(newTaskDone);
                if ($(this).children(".delete-new-task").length == 0){
                    $(this).append("<input type = 'button' value = 'Delete' class = 'delete-new-task' onClick = 'deleteNewTask(this);'>");

                }
            }
        })
        //$(".newTasks").append(newTaskDesc);
        //$(".newTasks").append(newTaskDone);
        
    })

})
$(".delete-new-task").each(function(){
    $(this).on("click", function(){
        console.log(totalForms);
        totalForms -=1;
        document.getElementById("id_form-TOTAL_FORMS").value = totalForms.toString();
        $(this).closest('div').remove();
    })
})

function deleteNewTask(doc){
    doc.closest('div').remove();
}