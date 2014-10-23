(function(jQuery) {
    jQuery.fn.uapply = function(options) {
        var matchedObject = this;

        var toggler = jQuery(".toggler", matchedObject);
        toggler.utoggler();
    };
})(jQuery);

(function(jQuery) {
    jQuery.fn.utoggler = function(options) {
        var matchedObject = this;
        matchedObject.click(function() {
                    var element = jQuery(this);
                    var _body = element.parents("body");

                    var isWide = _body.hasClass("uwide");
                    if (isWide) {
                        _body.removeClass("uwide");
                        element.text("maximize");
                    } else {
                        _body.addClass("uwide");
                        element.text("minimize");
                    }
                });
    };
})(jQuery);

jQuery(document).ready(function() {
            var _body = jQuery("body");
            _body.bind("applied", function(event, base) {
                        base.uapply();
                    });
        });
