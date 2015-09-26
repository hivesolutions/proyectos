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

                    var isIcon = element.hasClass("icon");
                    var isWide = _body.hasClass("uwide");
                    if (isWide) {
                        _body.removeClass("uwide");
                        element.removeClass("minimize");
                        !isIcon && element.text("maximize");
                    } else {
                        _body.addClass("uwide");
                        element.addClass("minimize");
                        !isIcon && element.text("minimize");
                    }
                });
    };
})(jQuery);

jQuery(document).ready(function() {
            var _body = jQuery("body");
            _body.bind("applied", function(event, base) {
                        // runs the initial apply operation so that the elements
                        // are registered for the domain specific operations
                        base.uapply();
                    });
            _body.bind("post_applied", function(event, base) {
                        // verifies if this is a global selection and if that's
                        // the case refreshes the location of the document so
                        // that any hash based scroll operation is now performed
                        // with the "new" look and feel (as expected)
                        var isBody = base.is("body");
                        isBody && setTimeout(function() {
                                    document.location.hash = document.location.hash;
                                });
                    });
        });
