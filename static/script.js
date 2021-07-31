let service_base_url = 'http://192.168.1.126:80'
let list_meeting_endpoint = 'get_meetings_list'

$.getJSON(service_base_url + "/" + list_meeting_endpoint, function(data) {
    $.each(data, function(index) {
    var trHTML = '';
    trHTML += '<tr><td><center>' +
    data[index].meeting_id + '</center></td><td><center>' +
    data[index].participants_amt + '</center></td></tr>';
    $('#meeting_list_table').append(trHTML);
    });
});

