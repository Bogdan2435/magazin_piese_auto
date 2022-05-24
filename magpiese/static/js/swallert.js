{% for msg in messages %}
    {% if msg.tags == "error" %}
    icn = "error"
    {% else %}
    icn = "success"
    {% endif %}
    swal({
        title: "{{ msg }}",
        text: "",
        icon: icn,
        button: "Inchide!",
    });
{% endfor %}