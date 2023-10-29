$(document).ready(async function () {
    $("#reg-form").submit(async function (event) {
        event.preventDefault();
        var form_data = $(this).serialize();
        try {
            const response = await fetch("{% url 'tracker:add_tracked_ajax' %}", {
                method: "POST",
                body: form_data,
            });
            const data = await response.json();

            if (data.status === 'success') {
                // Berhasil update tracker
                console.log(data.message);
                // Refresh show_tracked.html content
                $("#tracked-content").load("{% url 'tracker:show_tracked' %} #tracked-content");
            } else {
                console.error(data.message);
            }
        } catch (error) {
            console.error(error);
        }
    });
});
