```typescript
interface Bifunctor<A,B> {
    bimap<X,Y>(f: (A)=>X, g: (B)=>Y): Bifunctor<X,Y>;
}
class Pair<A, B> implements Bifunctor<A, B>{
    a: A
    b: B
    constructor(a: A, b: B) {
        this.a = a;
        this.b = b;
    }
    bimap(f, g) {
        return new Pair(f(this.a), g(this.b))
    }
    greet() {
        return `$`{this.a}:`${typeof this.a} $`{this.b}:`${typeof this.b}`
    }
}
let p1 = new Pair<number, boolean>(3, true)
let p2 = p1.bimap((x:number):string => x.toString(), (y:boolean):string => y.toString())
alert(p2.greet());
```