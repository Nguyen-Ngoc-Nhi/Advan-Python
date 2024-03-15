public class Person {
    String name;
    int age;
    Person(String name, int age) {
        this.name = name;
        this.age = age;
    }
    void print() {
        System.out.println("Name is " + this.name);
        System.out.println("Age is " + this.age);
    }
    void print(boolean nameOnly) {
        System.out.println("Name is " + this.name);
        if (!nameOnly)
            System.out.println("Age is " + this.age);
    }

    public static void main(String[] args) {
        Person macron = new Person("Macron", 48);
        macron.print();
    }
}