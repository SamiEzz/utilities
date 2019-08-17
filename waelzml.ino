int _a=4;
int _b=0;
int _c=8;
int _d=11;
int _e=10;
int _f=3;
int _g=7;
int _dp=9;
int _1=5;
int _2=2;
int _3=1;
int _4=6;
unsigned short int num=1489;
    
void setup(){
    pinMode(_a,OUTPUT);
    pinMode(_b,OUTPUT);
    pinMode(_c,OUTPUT);
    pinMode(_d,OUTPUT);
    pinMode(_e,OUTPUT);
    pinMode(_f,OUTPUT);
    pinMode(_g,OUTPUT);
    pinMode(_dp,OUTPUT);
    pinMode(_1,OUTPUT);
    pinMode(_2,OUTPUT);
    pinMode(_3,OUTPUT);
    pinMode(_4,OUTPUT);
    
}

void loop(){
    digitalWrite(_1,HIGH);
    digitalWrite(_2,HIGH);
    digitalWrite(_3,HIGH);
    digitalWrite(_4,HIGH);
    /*
    digitalWrite(_1,LOW);
    print_2();
    digitalWrite(_1,HIGH);
  */
    digitalWrite(_2,LOW);
    print_2();
    digitalWrite(_2,HIGH);
    delay(1);
    digitalWrite(_3,LOW);
    print_4();
    digitalWrite(_3,HIGH);
    delay(1);
    digitalWrite(_4,LOW);
    print_8();
    digitalWrite(_4,HIGH);
    delay(1);
}


void e_loop(){
    int m_delay=10;
    
    num+=1;
    
    afficher(num);
    delay(m_delay);
}


void afficher(int num){
    int u,d,c,m;
    m = (num - (num % 1000))/1000;
    c = (num - m - ((num-m)%100))/100;
    d = (num - m - c - ((num-m-c)%10))/10;
    u = num - m - c - d ;

    digitalWrite(_4,LOW);
    onedigit(m);
    digitalWrite(_4,HIGH);

    digitalWrite(_3,LOW);
    onedigit(c);
    digitalWrite(_3,HIGH);
    
    digitalWrite(_2,LOW);
    onedigit(d);
    digitalWrite(_2,HIGH);
    
    digitalWrite(_1,LOW);
    onedigit(u);
    digitalWrite(_1,HIGH);

}


void onedigit(int digit){
    switch (digit)
    {
    case 1:
        print_1();
        break;
    
    case 2:
        print_2();
        break;
    
    case 3:
        print_3();
        break;
    
    case 4:
        print_4();
        break;
    
    case 5:
        print_5();
        break;
    
    case 6:
        print_6();
        break;
    
    case 7:
        print_7();
        break;
    
    case 8:
        print_8();
        break;
    
    case 9:
        print_9();
        break;
    
    default:
        initdigits();

        break;
    }
    
}






void initdigits(){
    digitalWrite(_a,LOW);
    digitalWrite(_b,LOW);
    digitalWrite(_c,LOW);
    digitalWrite(_d,LOW);
    digitalWrite(_e,LOW);
    digitalWrite(_f,LOW);
    digitalWrite(_g,LOW);   
}

void print_1(){
    initdigits();
    digitalWrite(_b,HIGH);
    digitalWrite(_c,HIGH);
    
}
void print_2(){
    initdigits();
    digitalWrite(_a,HIGH);
    digitalWrite(_b,HIGH);
    digitalWrite(_g,HIGH);
    digitalWrite(_e,HIGH);
    digitalWrite(_d,HIGH);
    
}
void print_3(){
    initdigits();
    digitalWrite(_a,HIGH);
    digitalWrite(_b,HIGH);
    digitalWrite(_g,HIGH);
    digitalWrite(_c,HIGH);
    digitalWrite(_d,HIGH);
    
}
void print_4(){
    initdigits();
    digitalWrite(_f,HIGH);
    digitalWrite(_b,HIGH);
    digitalWrite(_g,HIGH);
    digitalWrite(_c,HIGH);
 
}
void print_5(){
    initdigits();
    digitalWrite(_a,HIGH);
    digitalWrite(_f,HIGH);
    digitalWrite(_g,HIGH);
    digitalWrite(_c,HIGH);
    digitalWrite(_d,HIGH);
    
}
void print_6(){
    initdigits();
    digitalWrite(_a,HIGH);
    digitalWrite(_f,HIGH);
    digitalWrite(_g,HIGH);
    digitalWrite(_e,HIGH);
    digitalWrite(_c,HIGH);
    digitalWrite(_d,HIGH);

    
}
void print_7(){
    initdigits();
    digitalWrite(_b,HIGH);
    digitalWrite(_c,HIGH);
    digitalWrite(_a,HIGH);
    
}
void print_8(){
    digitalWrite(_a,HIGH);
    digitalWrite(_f,HIGH);
    digitalWrite(_g,HIGH);
    digitalWrite(_e,HIGH);
    digitalWrite(_c,HIGH);
    digitalWrite(_d,HIGH);
    digitalWrite(_b,HIGH);
   
    
}
void print_9(){
    digitalWrite(_a,HIGH);
    digitalWrite(_f,HIGH);
    digitalWrite(_g,HIGH);
    digitalWrite(_e,LOW);
    digitalWrite(_c,HIGH);
    digitalWrite(_d,HIGH);
    digitalWrite(_b,HIGH);

    
}
