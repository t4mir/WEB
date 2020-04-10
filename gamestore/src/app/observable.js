class Newspaper {
    constructor(name) {
        this.name = name;
    }
    publishNews(name) {
        console.log(name);
    }
}
const nurkz = new Newspaper('Nur');

nurkz.publishNews('here i am');

class FashionNemsObservable {
    constructor() {
        this.subscribers = [];
    }
    subscribe(sub) {
        this.subscribers.push(sub);
    }
    delete (exSub) {
        this.subscribers = this.subscribers.filter(sub => sub !== exSub);
    }
    notify (news) {
        this.subscribers.forEach (Newspaper => nurkz.publishNews(news));
    }
}
const oriflame = new Newspaper('oriflame');
const glamour = new Newspaper('glamour');
const romero = new FashionNemsObservable();

romero.subscribe(oriflame);
romero.subscribe(glamour);

romero.notify('Marguese');
romero.delete(oriflame);