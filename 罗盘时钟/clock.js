// var now = new Date();
var yearText = ['']
var monthText = ["1月", "2月", "3月", "4月", "5月", "6月", "7月", "8月", "9月", "10月", "11月", "12月"];
var dayText = ["1日", "2日", "3日", "4日", "5日", "6日", "7日", "8日", "9日", "10日", "11日", "12日", "13日", "14日", "15日", "16日", "17日", "18日", "19日", "20日", "21日", "22日", "23日", "24日", "25日", "26日", "27日", "28日", "29日", "30日", "31日"];
var weekText = ["周日", "周一", "周二", "周三", "周四", "周五", "周六"];
var hourText = ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23"];
var minuteText = ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10",
    "11", "12", "13", "14", "15", "16", "17", "18", "19", "20",
    "21", "22", "23", "24", "25", "26", "27", "28", "29", "30",
    "31", "32", "33", "34", "35", "36", "37", "38", "39", "40",
    "41", "42", "43", "44", "45", "46", "47", "48", "49", "50",
    "51", "52", "53", "54", "55", "56", "57", "58", "59"];
var secondsText = ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10",
    "11", "12", "13", "14", "15", "16", "17", "18", "19", "20",
    "21", "22", "23", "24", "25", "26", "27", "28", "29", "30",
    "31", "32", "33", "34", "35", "36", "37", "38", "39", "40",
    "41", "42", "43", "44", "45", "46", "47", "48", "49", "50",
    "51", "52", "53", "54", "55", "56", "57", "58", "59"];

//时钟页面
var clock;

// 存放元素的数组
var yearList = [];
var monthList = [];
var dayList = [];
var weekList = [];
var hourList = [];
var minuteList = [];
var secondsList = [];

//二维数组 存放文字内容及页面显示标签
var textList = [
    [yearText, yearList],
    [monthText, monthList],
    [dayText, dayList],
    [weekText, weekList],
    [hourText, hourList],
    [minuteText, minuteList],
    [secondsText, secondsList],
]

//时钟页面样式
window.onload = function () {
    init();

    setTimeout(function () {
        initTransition();
    }, 0)

    setTimeout(function () {
        var timeArr = [0, 0, 0, 0, 0, 0, 0]
        rotateTransition(timeArr)
        setInterval(function () {
            runtime()
        }, 1000)
    }, 1000)
    // setInterval(function () {
    //     runtime()
    // }, 100)
};


function init() {

    clock = document.querySelector('#clock');

    for (var i in textList) {
        for (var j in textList[i][0]) {
            var temp = createLabel(textList[i][0][j]);
            clock.appendChild(temp);
            textList[i][1].push(temp);
        }
    }


    console.log(textList);

}

// 创建标签并将文字填充标签内 接收参数为文字内容
function createLabel(text) {
    var div = document.createElement('div');
    div.classList.add('label');
    div.innerText = text;
    return div;
}

function runtime() {

    var now = new Date();
    //当前时间获取
    var month = now.getMonth();
    var day = now.getDate();
    var week = now.getDay();
    var hour = now.getHours();
    var minute = now.getMinutes();
    var seconds = now.getSeconds();
    var timeArr = [0, month, day - 1, week, hour, minute, seconds]

    console.log(timeArr)
    clearColor();
    rotateTransition(timeArr);
    addColor(timeArr);
}


function addColor(timeArr) {

    // var label = document.querySelectorAll('.label')
    // for (var i in timeArr) {
    //     var len = i > 1 ? textList[i - 1][0].length : 0;
    //     var num = timeArr[i];
    //     var index = len + num;
    //     label[index].classList.add('now')
    //     // console.log(label[index])
    // }

    for (var i = 1; i < timeArr.length; i++) {
        var index = timeArr[i];
        // for (var j = 0; j < timeArr.length; j++) {
        //     var temp = textList[i][1][j];
        //     // var deg = 360 / textList[i][0].length * j;
        //     var deg = 360 / textList[i][0].length * (j - timeArr[i]);
        //     temp.style.transform = temp.style.transform.replace(/-?\d+deg/, deg + 'deg');
        //     // console.log(temp)
        // }
        textList[i][1][index].classList.add('now')
    }
}

function clearColor() {

    var now = document.querySelectorAll('.now');
    now.forEach(function (item) {
        item.classList.remove('now');
    })

}


function initTransition() {
    for (var i in textList) {
        for (var item of textList[i][1]) {
            item.style.transform = 'translate(' + i * 80 + 'px,-50%)'
            item.style.transformOrigin = -(i * 80) + 'px 50%';
        }
    }
}

function rotateTransition(timeArr) {
    for (var i in textList) {
        for (var j in textList[i][1]) {
            var temp = textList[i][1][j];
            var deg = 360 / textList[i][0].length * (j - timeArr[i]);
            temp.style.transform = 'translate(' + i * 80 + 'px,-50%)' + ' rotate(' + deg + 'deg)';
        }
    }
}