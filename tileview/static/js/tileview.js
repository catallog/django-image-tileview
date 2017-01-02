if (typeof jQuery === 'undefined') {
    var jQuery = django.jQuery;
}

jQuery( document ).ready(function() {

    jQuery('#select_all').click( function() {
        jQuery('#changelist-form input[type=checkbox]').each(function(){
            var c = jQuery(this);
            c.prop("checked", !c.prop("checked"));
        });
    });

});
