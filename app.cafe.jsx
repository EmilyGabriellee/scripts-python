import * as React from 'react';
import {StyleSheet,Image,ScrollView,Text,View} from 'react-native';

export default class App extends React.Component {
state = {};
customStyle = StyleSheet.create({ custom: {  flex: 1,
  backgroundColor: "#ffff99",
} });

custumimageStyle = StyleSheet.create({ custumimage: {  width: "100%",
  height: "25%",
} });

customScrollStyle = StyleSheet.create({ customScroll: {  padding: 10,
} });

componentDidMount() {this.events = Object.getOwnPropertyNames(this.__proto__).filter(function(event) {
        return event.indexOf("_event") != -1;
    });
this.events.forEach(function(method) {
        this[method]();
    }, this);}
render() {  return (

  <View style = {this.customStyle.custom}>

    <Image resizeMode="stretch" style = {this.custumimageStyle.custumimage} source={{uri: "https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2F2.bp.blogspot.com%2F_LciCOC_smYQ%2FTGEn0pc4eVI%2FAAAAAAAAABQ%2F_DjfdaNfxPM%2Fs1600%2FBalmoral-milk-bar-1.jpg&f=1&nofb=1"}}></Image>
    <ScrollView style = {this.customScrollStyle.customScroll}>

      <Text style = {{margin: 10, fontSize: 20, fontWeight: "bold", textAlign: "center", color: "#9999ff"}}>{"M E N U  "}</Text>
      <Text style={{margin: 2}}>{""}</Text>
      <Text style={{margin: 2}}>{""}</Text>
      <Text style = {{margin: 10, fontSize: 20, fontWeight: "bold", textAlign: "center", color: "#ffccff"}}>{"- - S A L G A DO S - -"}</Text>
      <Text style={{margin: 2}}>{"pao de queijo"}</Text>
      <Text style={{margin: 2}}>{"coxinha"}</Text>
      <Text style={{margin: 2}}>{"bolinho de queijo"}</Text>
      <Text style={{margin: 2}}>{"bolinho de presunto e queijo"}</Text>
      <Text style={{margin: 2}}>{"quibe"}</Text>
      <Text style={{margin: 2}}>{"pastel"}</Text>
      <Text style={{margin: 2}}>{"pao francês"}</Text>
      <Text style={{margin: 2}}>{""}</Text>
      <Text style={{margin: 2}}>{""}</Text>
      <Text style = {{margin: 10, fontSize: 20, fontWeight: "bold", textAlign: "center", color: "#99ff99"}}>{"- - D O C E S - -"}</Text>
      <Text style={{margin: 2}}>{"pao doce "}</Text>
      <Text style={{margin: 2}}>{"brigadeiro"}</Text>
      <Text style={{margin: 2}}>{"beijinho"}</Text>
      <Text style={{margin: 2}}>{"pudin"}</Text>
      <Text style={{margin: 2}}>{""}</Text>
      <Text style={{margin: 2}}>{""}</Text>
      <Text style = {{margin: 10, fontSize: 20, fontWeight: "bold", textAlign: "center", color: "#66ffff"}}>{"- - B E B I D A S - -"}</Text>
      <Text style={{margin: 2}}>{""}</Text>
      <Text style = {{margin: 10, fontSize: 20, fontWeight: "bold", textAlign: "center", color: "#3366ff"}}>{"- G E L A D A S -"}</Text>
      <Text style={{margin: 2}}>{"coca-cola"}</Text>
      <Text style={{margin: 2}}>{"sprite"}</Text>
      <Text style={{margin: 2}}>{"fanta"}</Text>
      <Text style={{margin: 2}}>{"dolly"}</Text>
      <Text style={{margin: 2}}>{"chá gelado"}</Text>
      <Text style={{margin: 2}}>{"água"}</Text>
      <Text style={{margin: 2}}>{""}</Text>
      <Text style = {{margin: 10, fontSize: 20, fontWeight: "bold", textAlign: "center", color: "#000099"}}>{"- Q U E N T E S -"}</Text>
      <Text style={{margin: 2}}>{"café"}</Text>
      <Text style={{margin: 2}}>{"caputino"}</Text>
      <Text style={{margin: 2}}>{"chocolate"}</Text>
      <Text style={{margin: 2}}>{"leite"}</Text>
      <Text style={{margin: 2}}>{"chá"}</Text>
    </ScrollView>

  </View>

);
}
}