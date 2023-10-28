$(document).ready(async function () {
    $("#reg-form").submit(async function (event) {
        event.preventDefault();
        var form_data = $(this).serialize();
        try {
            const response = await fetch("{% url 'tracker:add_tracked' %}", {
                method: "POST",
                body: form_data,
            });
            const data = await response.json();
            // Refresh show_tracked.html content
            $("#tracked-content").load("{% url 'tracker:show_tracked' %} #tracked-content");
        } catch (error) {
            console.error(error);
        }
    });
});
