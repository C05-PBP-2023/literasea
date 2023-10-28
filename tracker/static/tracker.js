$(document).ready(function () {
    $("#reg-form").submit(function (event) {
        event.preventDefault();
        var form_data = $(this).serialize();
        $.ajax({
            type: "POST",
            url: "{% url 'tracker:add_tracked' %}",
            data: form_data,
            success: function (data) {
                // Refresh show_tracked.html content
                $("#tracked-content").load("{% url 'tracker:show_tracked' %} #tracked-content");
            }
        });
    });
});
