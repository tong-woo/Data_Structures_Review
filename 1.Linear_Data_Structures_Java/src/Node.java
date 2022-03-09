public class Node {
    public String data;
    private Node next;
    private Node previous;


    public Node(String data){
        this.data = data;
        this.next = null;
    }
    public void setNextNode(Node node){
        this.next = node;
    }

    public Node getNextNode(){
        return this.next;
    }

    public void setPreviousNode(Node node) {
        this.previous = node;
    }

    public Node getPreviousNode() {
        return this.previous;
    }
    public static void main(String[] args){
        Node firstNode = new Node("I am a Node!");
        System.out.println(firstNode.data);
        System.out.println(firstNode.next);
        Node secondNode = new Node("I am the second Node!");
        firstNode.setNextNode(secondNode);
        System.out.print(firstNode.next.data);
        System.out.println(firstNode.getNextNode().data);

    }
}
