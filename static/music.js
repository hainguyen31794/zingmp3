function getlink () {
    let url = document.querySelector("input").value;
    let ispl = document.getElementById("ispl").checked;

    let result = url.match(/([\w\d]+)(?=.html)/g);
    if (result){
        fetch(`/music?id=${result}&ispl=${ispl}`)
        .then(res => res.text())
        .then(body => {
            let textarea = document.querySelector("textarea");
            textarea.innerHTML = body
        })
        .catch(err => console.log("that bai"));
    }else{
        console.log("that bai");
    }
};





