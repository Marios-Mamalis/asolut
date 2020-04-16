const pieces = {0:  ["adjective or numeral, ordinal", "adjective, comparative", "adjective, superlative"],
          1: ["noun, common, singular or mass", "noun, proper, singular", "noun, proper, plural", "noun, common, plural"],
          2: ["pronoun, personal", "pronoun, possessive"],
          3: ["adverb", "adverb, comparative", "adverb, superlative"],
          4: ["verb, base form", "verb, past tense", "verb, present participle or gerund", "verb, past participle", "verb, present tense, not 3rd person singular", "verb, present tense, 3rd person singular"],
          5: ["WH-determiner", "WH-pronoun", "WH-pronoun, possessive", "Wh-adverb"],
          6: ["symbol", "numeral, cardinal", "list item marker"],
          7: ["conjunction, coordinating", "determiner", "existential there", "preposition or conjunction, subordinating", "modal auxiliary",
          "pre-determiner", "'to' as preposition or infinitive marker", "interjection", "particle", "gentive marker", "foreign word"]
          }

const codes = {0:  ["JJ", "JJR", "JJS"],
          1: ["NN", "NNP", "NNPS", "NNS"],
          2: ["PRP", "PRP$"],
          3: ["RB", "RBR", "RBS"],
          4: ["VB", "VBD", "VBG", "VBN", "VBP", "VBZ"],
          5: ["WDT", "WP", "WP$", "WRB"],
          6: ["SYM", "CD", "LS"],
          7: ["CC", "DT", "EX", "IN", "MD",
          "PDT", "TO", "UH", "RP", "POS", "FW"]
          }          

const cats = ["adjectives", "nouns", "pronouns", "adverbs", "verbs", "wh-words", "symbols", "ect"]

document.addEventListener("click", function(){
    document.getElementById("encoding_items").innerHTML = "";
    for(var i = 0; i < 8; i++) {
        document.querySelector("div#" + ("b" + i + "elements")).style.visibility = "hidden";
    }
  });


function upnu() {
    document.getElementById("numbersbars").stepUp(1);
}

function donu() {
    if(document.getElementById("numbersbars").value < 2) {
        document.getElementById("numbersbars").value = 1
    } else {
        document.getElementById("numbersbars").stepDown(1);
    }
}

async function get_file_name() {  
    let n = await eel.open_file()();
    document.getElementById("file_name").innerHTML = n
    document.getElementById("errortextfile").style.visibility = "hidden";
}

function change_description_mode() {
    const array_mode = ["Keep all characters", 
                        "Remove symbols at the end <br /> and the start", 
                        "Remove symbols at the end <br /> and the start with exceptions <br /> for common meaningful symbols", 
                        "Remove all symbols"]
    var x = document.getElementById("sub").value;
    document.getElementById("select_desc").innerHTML = array_mode[x-1];
  }

function change_description_sort() {
    const array_sort = ["Sort the bars by the order of the words' frequencies (regular word frequency)", 
                        "Sort the bars by the order of the words' synonyms' frequencies", 
                        "Sort the bars by the order of the sum of the words' synonyms' frequencies and the words' frequencies"]
    var x = document.getElementById("sor").value;
    document.getElementById("sort_descr").innerHTML = array_sort[x-1]
}

function boxes(iid) {
  if (document.querySelector("div#" + iid.substring(0, 2) + "elements").style.visibility=="visible") {
      document.querySelector("div#" + iid.substring(0, 2) + "elements").style.visibility = "hidden";
  } else {
      document.querySelector("div#" + iid.substring(0, 2) + "elements").style.visibility = "visible";
  }
}

function mark(iid, chk) {
  for(var i = 0; i < 11; i++) {
      document.querySelector("input#" + iid.substring(0, 2) + "e" + i).checked = chk;
  }
}

async function autocomplete_enc() {
    let enc = await eel.encs()();
    var newenc = enc.filter(itemm => itemm.match(RegExp(document.getElementById("encoding_input").value, "i")));
    document.getElementById("encoding_items").innerHTML = "";
    if(document.getElementById("encoding_input").value != "") {
        for(var i = 0; (i < newenc.length && i < 5); i++) {
            var newp = document.createElement("div");
            newp.innerHTML = newenc[i];
            newp.id = "newp" + i;
            newp.tabIndex = 1;
            newp.onclick = function() {
                document.getElementById("encoding_input").value = document.getElementById(this.id).innerHTML;
            };
            document.getElementById("encoding_items").appendChild(newp);
        }
    }
}

document.addEventListener("DOMContentLoaded", function(event) {
    for(var i=0; i<Object.values(pieces).length; i++) {
         var inne = Object.values(pieces)[i];
         var divcontainer = document.createElement("div");
         divcontainer.className = ("box_container");
         divcontainer.id = "b" + i + "container";
         var divheader = document.createElement("div");
         divheader.className = "box_headers";
         divheader.id = "b" + i + "header";
         var checkboxTitle = document.createElement("input");
         checkboxTitle.className = ("checkbox_title");
         checkboxTitle.id = "b" + i + "name";
         checkboxTitle.setAttribute("type", "checkbox");
         checkboxTitle.onclick = function() {
              mark(this.id, this.checked);
         };
         checkboxTitle.value = cats[i];
         var labelTitle = document.createElement("label");
         labelTitle.setAttribute("for", "b" + i + "name");
         labelTitle.innerHTML = cats[i];
         var gearTitle = document.createElement("input");
         gearTitle.className = "gear";
         gearTitle.setAttribute("type", "image");
         gearTitle.id = "b" + i + "gear";
         gearTitle.src = "images/gear.svg";
         gearTitle.onclick = function(event) {
              boxes(this.id);          
              event.stopPropagation();    
          };
         var divelements = document.createElement("div");
         divelements.id = "b" + i + "elements";
         divelements.className = "box_elements";
         divelements.onclick = function(event) {       
            event.stopPropagation();    
        };
      for(var elemInd in inne) {
              var checkboxElem = document.createElement("input");
              checkboxElem.id = "b" + i + "e" + elemInd;
              checkboxElem.className = ("checkbox_elem");
              checkboxElem.setAttribute("type", "checkbox");
              checkboxElem.setAttribute("for", "b" + i + "e" + elemInd);
              checkboxElem.value = Object.values(codes)[i][elemInd];
              var labelElem = document.createElement("label");
              labelElem.innerHTML = Object.values(pieces)[i][elemInd];
              var br = document.createElement('br');
              divelements.appendChild(checkboxElem);
              divelements.appendChild(labelElem);
              divelements.appendChild(br);
         };
         divheader.appendChild(checkboxTitle);
         divheader.appendChild(labelTitle);
         divheader.appendChild(gearTitle);
         divcontainer.appendChild(divheader);
         divcontainer.appendChild(divelements);
         document.getElementById("pos_boxes_container").appendChild(divcontainer);
    };
    document.getElementById("numbersbars").addEventListener("focusout", function() {
        document.getElementById("numbersbars").value = Math.floor(document.getElementById("numbersbars").value);
        if(document.getElementById("numbersbars").value < 1) {
            document.getElementById("numbersbars").value = 1
        }
    });
});

eel.expose(get_to_python);
function get_to_python() {
    wrapper = []
    // encoding
    document.getElementById("errortext").style.visibility = "hidden";
    document.getElementById("errortextfile").style.visibility = "hidden";
    if(document.getElementById("encoding_input").value == "" && document.getElementById("file_name").innerHTML == "") {
            document.getElementById("errortext").style.visibility = "visible";
            document.getElementById("errortextfile").style.visibility = "visible";
    } else if(document.getElementById("file_name").innerHTML == "") {
        document.getElementById("errortextfile").style.visibility = "visible";
    } else if(document.getElementById("encoding_input").value == "") {
        document.getElementById("errortext").style.visibility = "visible";
    } else {
        // start it
        document.getElementById("loading_screen").style.visibility = "visible";
        document.getElementById("loading_screen").style.opacity = "1";

        wrapper.push(document.getElementById("encoding_input").value)
        // mode
        wrapper.push(document.getElementById("sub").value);
        // keep
        wrapper.push(document.getElementById("keepswitch").checked);
        // pos
        pos = []
        for(var i = 0; i < Object.values(pieces).length; i++) {
            for(var j = 0; j < Object.values(pieces[i]).length; j++) {
                if(document.querySelector("input#" + ("b"+ i + "e" + j)).checked == true) {
                    pos.push(document.querySelector("input#" + ("b"+ i + "e" + j)).value);
                }
            }
        }
        wrapper.push(pos);
        // sort
        wrapper.push(document.getElementById("sor").value);
        // numb
        wrapper.push(document.getElementById("numbersbars").value);
        return wrapper
    }
}

eel.expose(endit)
function endit() {
    document.getElementById("loading_screen").style.visibility = "hidden";
    document.getElementById("loading_screen").style.opacity = "0";
}
