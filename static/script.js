let service_base_url = 'http://192.168.1.126:80'
let list_meeting_endpoint = 'get_meetings_list'
let meetings_status_endpoint = 'stop_meeting'

function stop_meeting(meeting_id_to_delete) {
    $.ajax({
        type: 'PUT',
        url: service_base_url + "/" + meetings_status_endpoint + "/" + meeting_id_to_delete,
        success: function (response) {
        },
        error: function () {
        }
    })
};



$(document).ready(function(){
    $('body').on('click', '.stop_meeting', function() {
    var meeting_id_to_delete = $(this).context.id;
    stop_meeting(meeting_id_to_delete);
    });
});



$.getJSON(service_base_url + "/" + list_meeting_endpoint, function(data) {
    $.each(data, function(index) {
    var trHTML = '';
    trHTML += '<tr><td><center>' +
    data[index].meeting_id + '</center></td><td><center>' +
    data[index].participants_amt + '</center></td>' +
    '<td><button class=stop_meeting id=' + data[index].meeting_id  + '>Stop Meeting</button></td>';
    $('#meeting_list_table').append(trHTML);
    });
});

