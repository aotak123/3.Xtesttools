let monthText = ["1月", "2月", "3月", "4月", "5月", "6月", "7月", "8月", "9月", "10月", "11月", "12月"];
let dayText = ["1日", "2日", "3日", "4日", "5日", "6日", "7日", "8日", "9日", "10日", "11日", "12日", "13日", "14日", "15日", "16日", "17日", "18日", "19日", "20日", "21日", "22日", "23日", "24日", "25日", "26日", "27日", "28日", "29日", "30日", "31日"];
let weekText = ["周日", "周一", "周二", "周三", "周四", "周五", "周六"];
let hourText = ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23"];
let minuteText = ["00","01", "02", "03", "04", "05", "06", "07", "08", "09", "10",
    "11", "12", "13", "14", "15", "16", "17", "18", "19", "20",
    "21", "22", "23", "24", "25", "26", "27", "28", "29", "30",
    "31", "32", "33", "34", "35", "36", "37", "38", "39", "40",
    "41", "42", "43", "44", "45", "46", "47", "48", "49", "50",
    "51", "52", "53", "54", "55", "56", "57", "58", "59"];
let secondText = ["00","01", "02", "03", "04", "05", "06", "07", "08", "09", "10",
    "11", "12", "13", "14", "15", "16", "17", "18", "19", "20",
    "21", "22", "23", "24", "25", "26", "27", "28", "29", "30",
    "31", "32", "33", "34", "35", "36", "37", "38", "39", "40",
    "41", "42", "43", "44", "45", "46", "47", "48", "49", "50",
    "51", "52", "53", "54", "55", "56", "57", "58", "59"];

// 存放dom元素的数组
let monthList = [];
let dayList = [];
let weekList = [];
let hourList = [];
let minuteList = [];
let secondList = [];

//二维数组 存放文字内容及页面显示标签
let timeTextSet = [
    [monthText, monthList],
    [dayText, dayList],
    [weekText, weekList],
    [hourText, hourList],
    [minuteText, minuteList],
    [secondText, secondList]
];

// 判断是否为旋转页面
let isRotating = false;

//时钟页面
let clock;

window.onload = function () {
    init();
    // 每隔100ms获得 当前时间
    setInterval(function () {
        runTime();
    }, 200);

    // 旋转之前定位到当前时间
    locateCurrent();
    // 3秒后变成旋转样式
    setTimeout(function () {
        toRotate();
    }, 0);  //1000s
}

// 初始化函数
function init() {
    clock = document.getElementById('clock');
    // 生成标签 存放文字展示
    for (let i = 0; i < timeTextSet.length; i++) {
        for (let j = 0; j < timeTextSet[i][0].length; j++) {
            let temp = createLabel(timeTextSet[i][0][j]);
            clock.appendChild(temp);
            // 将生成的标签存放在数组list中
            timeTextSet[i][1].push(temp);
        }
    }

}

// 创建标签并将文字填充标签内 接收参数为文字内容
function createLabel(text) {
    let div = document.createElement('div');
    div.classList.add('label');
    div.innerText = text;
    return div;
}

function runTime() {
    //当前时间获取
    let now = new Date();
    let month = now.getMonth();
    let day = now.getDate();
    let week = now.getDay();
    let hour = now.getHours();
    let minute = now.getMinutes();
    let seconds = now.getSeconds();
    // 初始化时间颜色 并将走过的时间设置为黑色
    initStyle();

    // 当前时间设为与背景色对比度高一点的颜色
    // 将当前时间月份存放在数组中
    let nowValue = [month, day - 1, week, hour, minute, seconds];
    for (let i = 0; i < nowValue.length; i++) {
        let num = nowValue[i];
        timeTextSet[i][1][num].style.color = 'red';
        timeTextSet[i][1][num].style.fontSize = "36px";
    }

    // 变成旋转时钟
    if (isRotating) {
        // 圆心位置确定
        let widthMid = document.body.clientWidth / 2;
        let heightMid = document.body.clientHeight / 2;
        // 将每一个dom元素确定到圆的位置
        for (let i = 0; i < timeTextSet.length; i++) {
            for (let j = 0; j < timeTextSet[i][0].length; j++) {
                // 计算出每一个元素的位置  x y 坐标，圆的半径与时分秒的位置有关
                let r = (i + 1.5) * 50 + 40 * i;
                // 计算每一个平均的角度  将每一个单位对齐,再转化成弧度
                let deg = 360 / timeTextSet[i][1].length * (j - nowValue[i]);
                // 计算dom元素的坐标
                let x = r * Math.sin(deg * Math.PI / 180) + widthMid;
                let y = heightMid - r * Math.cos(deg * Math.PI / 180);
                // 样式
                let temp = timeTextSet[i][1][j];
                temp.style.transform = 'rotate(' + (-90 + deg) + 'deg)';
                temp.style.left = x + 'px';
                temp.style.top = y + 'px';
            }
        }
    }
}

function initStyle() {
    // 将所有数字内容置为白色
    let label = document.getElementsByClassName('label');
    for (let i = 0; i < label.length; i++) {
        label[i].style.color = 'white';
        label[i].style.fontSize = "24px";
    }
}


function locateCurrent() {
    for (let i = 0; i < timeTextSet.length; i++) {
        for (let j = 0; j < timeTextSet[i][1].length; j++) {
            // 获取原来的位置  再修改position 设置left top
            let tempX = timeTextSet[i][1][j].offsetLeft + "px";
            let tempY = timeTextSet[i][1][j].offsetTop + "px";
            // console.log(timeTextSet[i][1][j]);
            // 利用let 防止闭包
            setTimeout(function () {
                timeTextSet[i][1][j].style.position = "absolute";
                timeTextSet[i][1][j].style.left = tempX;
                timeTextSet[i][1][j].style.top = tempY;
            }, 50);
        }
    }
}

function toRotate() {
    isRotating = true;
    clock.style.transform = "rotate(90deg)";
}