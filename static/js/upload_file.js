function checkTagValidation() {
    let tag_input = document.getElementById("tag_input");
    let reg_invalid_tag = new RegExp(/[\\\/\?\:\"\|\*]/);
    if(tag_input.value==""){
        alert("input some tag");
        return false;
    }
    if (reg_invalid_tag.test(tag_input.value)) {
        alert("a tag cannot contain characters as follow:\
      \n\\  \/  \?  \:  \"  \|  \*")
        alert("no pass ========");
        return false;
    }
    let reg_seperators = new RegExp(/\s*[\,+\，+\;+\；+]\s*/);
    let tag_split = tag_input.value.split(reg_seperators);
    let tag_array = []
    for (let tag of tag_split) {
        if (tag == "") continue;
        tag_array.push(tag);
    }
    tag_input.value = tag_array.toString();
    return true;
}