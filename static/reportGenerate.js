/**
 * Created by alexandr on 31.08.15.
 */
$(document).ready(function(){
    $("#report_crash").tablesorter();
    $("#status").text("Будет использоваться для расчетов.");
    $(function(){
    $('#link_to_report').click(function(){
        $('#summary_report').slideToggle();
    });
});

    var effect = 100;
    var effect_in_business = 100;
    var effect_not_in_business = 100;
    var counter = 0;
     $('.effect_col').each(function() {
        effect -= parseFloat( $(this).text().replace(',', '.'));
        counter += 1;
    });
    $('.effect_in_business_col').each(function() {
        effect_in_business -= parseFloat( $(this).text().replace(',', '.'));
        });
    $('.effect_not_in_business_col').each(function() {
        effect_not_in_business -= parseFloat( $(this).text().replace(',', '.'));
        });
    effect = Math.round(effect*10000)/10000;
    effect_in_business = Math.round(effect_in_business*10000)/10000;
    effect_not_in_business = Math.round(effect_not_in_business*10000)/10000;
    $("#summary_effect").text("Доступность услуг: " + effect + "%");
    $("#summary_effect_in_business").text("Доступность услуг в бизнес время: " + effect_in_business + "%");
    $("#summary_effect_not_business").text("Доступность услуг не в бизнес время: " + effect_not_in_business + "%");
    $("#crash_quantity").text("За месяц призошло: " + counter + " аварий");


    $(function() {
        $('.checkbox_status').bind('click', function () {
        if (!$(this).is(":checked")) {
            var current = $(this).attr('id');
            var current_id = $(this).attr('id').slice(8);
            $('#' + current + 'text').text('Для расчетов не используются');
            var new_effect = parseFloat($("#summary_effect").text().slice(19)) - parseFloat($('#effect' + current_id).text().replace(',', '.'));
            new_effect = Math.round(new_effect*10000)/10000;
            var new_effect_in_business = parseFloat($("#summary_effect_in_business").text().slice(34)) - parseFloat($('#effect_in_business' + current_id).text().replace(',', '.'));
            new_effect_in_business  = Math.round(new_effect_in_business*10000)/10000;
            var new_effect_not_in_business = parseFloat($("#summary_effect_not_business").text().slice(37)) - parseFloat($('#effect_not_in_business' + current_id).text().replace(',', '.'));
            new_effect_not_in_business  = Math.round(new_effect_not_in_business*10000)/10000;
            $('#summary_effect').text("Доступность услуг: " + new_effect + "%" );
            $('#summary_effect_in_business').text("Доступность услуг в бизнес время: " + new_effect_in_business + "%" );
            $('#summary_effect_not_business').text("Доступность услуг не в бизнес время: " + new_effect_not_in_business + "%" );


        }else{
            var current = $(this).attr('id');
            var current_id = $(this).attr('id').slice(8);
            $('#' + current + 'text').text('');
            var new_effect = parseFloat($("#summary_effect").text().slice(19)) + parseFloat($('#effect' + current_id).text().replace(',', '.'));
            new_effect = Math.round(new_effect*10000)/10000;
            var new_effect_in_business = parseFloat($("#summary_effect_in_business").text().slice(34)) + parseFloat($('#effect_in_business' + current_id).text().replace(',', '.'));
            new_effect_in_business  = Math.round(new_effect_in_business*10000)/10000;
            var new_effect_not_in_business = parseFloat($("#summary_effect_not_business").text().slice(37)) + parseFloat($('#effect_not_in_business' + current_id).text().replace(',', '.'));
            new_effect_not_in_business  = Math.round(new_effect_not_in_business*10000)/10000;
            $('#summary_effect').text("Доступность услуг: " + new_effect + "%" );
            $('#summary_effect_in_business').text("Доступность услуг в бизнес время: " + new_effect_in_business + "%" );
            $('#summary_effect_not_business').text("Доступность услуг не в бизнес время: " + new_effect_not_in_business + "%" );
            $('.current_crash' + current_id).removeClass('.deactivated_col');
        }
    });
});

});

