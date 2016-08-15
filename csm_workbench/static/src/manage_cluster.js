$(function(){
    console.log("Start Manage Cluster!");
})

// show or hide the modal
$("#mCreateCluster")
    .on('shown.bs.modal', function () {
        console.log("Show The Modal!");
    })
    .on('hidden.bs.modal', function () {
        //reset the step
        wizardStepIndex = 0; 
        selectedStep(); 
        // clean the add storage group items
        $(".sg-item-more").remove();
        $(".sg-name").val("");
        $(".sg-value").val("ssd");
        $(".sg-add").show();
        $(".sg-remove").hide();
        console.log("Hidden The Modal!");
    });


// control the wizard steps
var wizardStepIndex = 0;
var wizardStepCount = 3;
$("#btnLastWizard").click(function(){
    if(wizardStepIndex == 0)
        return;    
    wizardStepIndex --;
    selectedStep();
});

$("#btnNextWizard").click(function(){
    if(wizardStepIndex == wizardStepCount)
        return;
    wizardStepIndex ++;
    selectedStep();
});

function selectedStep(){
    $(".wizard-pf-steps-indicator>li").each(function(index,element){
        if(wizardStepIndex == index)
            element.className = "active";
        else
            element.className = "";
    });

    $(".wizard-pf-main").each(function(index,element){
        if(wizardStepIndex == index)
            element.className = "wizard-pf-main";
        else
            element.className = "wizard-pf-main hidden";
    });

    //if current step is setting server
    if (wizardStepIndex == 2)
        $(".wizard-pf-sidebar")[0].className = "wizard-pf-sidebar";
    else
        $(".wizard-pf-sidebar")[0].className = "wizard-pf-sidebar hidden";
}

//about cluster storage group method
var sgItemHTML = "<tr class=\"sg-item sg-item-more\">"+
                "    <td><input type=\"text\" class=\"form-control sg-name\" /></td>"+
                // "    <td><input type=\"text\" class=\"form-control sg-value\" /></td>"+
                "    <td>" +
                "       <select class=\"form-control sg-value\">" +
                "           <option value=\"ssd\">ssd</option>" +
                "           <option value=\"1500\">1500</option>" +
                "       </select>" +
                "    </td>" +
                "    <td>"+
                "        <span class=\"fa fa-times-circle fa-font-20 sg-remove\" style=\"display:none\" onclick=\"removeSGItem(this)\"></span>"+
                "        <span class=\"fa fa-plus-circle  fa-font-20 sg-add\" onclick=\"addSGItem()\"></span>"+
                "    </td>"+
                "</tr>";

function addSGItem(){
    // first of all, hide all the add button
    $(".sg-add").hide();
    // add the storage group table.row
    $("#tCSG>tbody").append(sgItemHTML);
    // show the remove button
    $(".sg-remove").show();
};

function removeSGItem(sender){
    // get the row of storage group item
    // and remove it 
    var sgItem = sender.parentNode.parentNode;
    sgItem.remove();
    
    // check the storage group count
    if($(".sg-item").length==1){
        $(".sg-remove").hide();
        $(".sg-add").show();
    }
}