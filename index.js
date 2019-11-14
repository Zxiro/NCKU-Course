var linebot=require(linebot)
var express=require(express)

var bot=linebot({
    Id:"1653531104",
    Secret:"88a6f30705ff03a09f651ff01b72987c",
    AccessToken:"Bvs/Y3g3UEkpOyx+RUKcjRbEOoLZbFE07ni4+W8TyXjAXEgwmFh0DYwy+VkP8pWRZj4zUZ/qOdt2cLFog8KVPlaPefEMKf32y3PkTYx4SICtKg4mx7Evg7hwWQywaPu+ErLRQvAqxqAb7VtpsckLsAdB04t89/1O/w1cDnyilFU="
});

bot.on('message',function(event){
    //event.message.text 是使用者傳給linebot 的訊息
    //event.reply('linebot想要傳回給使用者的訊息')
    event.reply(event.message.text).then(function(data){

    }).catch(function(err){
    event.reply('fail')
    });
});
