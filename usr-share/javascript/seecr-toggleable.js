
function toggleElement(elm, divId) {
    $("#" + divId).toggleClass('show');
    $(elm).toggleClass('show');
}

function openElementInHash() {
    $("h3.toggleable").each(function(i, elm) {
        elm.onclick = function() { toggleElement(elm, "div_" + elm.id); }
    });
    if(window.location.hash) {
        var divId = window.location.hash.substring(1);
        console.log($('#'+divId));
        toggleElement($('#'+divId)[0], "div_"+divId);
    }
}
window.onload = openElementInHash;