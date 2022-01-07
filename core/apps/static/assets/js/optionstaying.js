$(function() {
    var selectOptions;
    if(localStorage.getItem("selectOptions")) {
        selectOptions = JSON.parse(localStorage.getItem("selectOptions"));
        Object.keys(selectOptions).forEach(function(select) {
          $("select[name="+select+"]").val(selectOptions[select]);
        });
   } else {
      selectOptions = {};
   }
   $("select").change(function() {
        var $this =  $(this),
            selectName = $this.attr("name");
       selectOptions[selectName] = $this.val();
       localStorage.setItem("selectOptions", JSON.stringify(selectOptions));
     });
 
 });
