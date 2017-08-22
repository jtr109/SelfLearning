//index.js
//获取应用实例
var helloData = {
  name: 'WeChat'
}

Page({
  data: helloData,
  changeName: function(e) {
    this.setData({
      name: 'MINA'
    })
  }
})
