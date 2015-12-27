/**
 * Created by Takamichi on 12/27/15.
 */
jQuery(document).ajaxSend(function(event, xhr, settings) {
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    function sameOrigin(url) {
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }
    function safeMethod(method) {
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    if (!safeMethod(settings.type) && sameOrigin(settings.url)) {
        xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
    }
});


$(function() {

    var change_point = function(id, isLike) {
        var data = {
            'sbj-id': id,
            'action': 'point',
            'isLike': isLike
        };

        $.ajax({
            'url': '/changepoint/',
            'type': 'POST',
            'data': JSON.stringify(data),
            'success': function() {
                var current_point = $('#count-' + id).text();
                //socket.send(data)
            },
            'error': function(e) {
                console.log(e);
            }
        })
    };

    var countup = function(data) {
        var count = $('#count-' + data['sbj-id']);
        var current_point = count.text();
        count.text(Number(current_point) + 1);
    };

    var countdown = function(data) {
        var count = $('#count-' + data['sbj-id']);
        var current_point = count.text();
        count.text(Number(current_point) - 1);
    };

    var socket;

    var pointed = function(data) {
        if (data.isLike == 1) {
            countup(data);
        } else {
            countdown(data);
        }
    };

    var connected = function() {
        // do something when connected
    }

    var disconnected = function() {
        setTimeout(start, 1000);
    };

    var start = function() {
        socket = new io.Socket();
        socket.connect();
        socket.on('connect', connected);
        socket.on('disconnect', disconnected);
        socket.on('message', pointed);
    };

    $('[id^=up]').on('click', function() {
        change_point($(this).data('sbj-id'), 1);
    });
    $('[id^=down]').on('click', function() {
        change_point($(this).data('sbj-id'), 0);
    } );

    start();

});