import java.util.List;

/**
 *
 * we want the linked listto be able to:
 * add a new node to the beginning (head) of the list
 * add a new node to the end (tail) of the list
 * remove a node from the beginning (head) of the list
 * print out the nodes in the list in order from head to tail
 *
 */


public class LinkedList {

    public Node head;

    public void addToHead(String data) {
        Node newHead = new Node(data);
        Node currentHead = this.head;
        this.head = newHead;
        if (currentHead != null) {
            this.head.setNextNode(currentHead);
        }
    }

    public void addToTail(String data){
        Node tail = this.head;
        if (tail == null){
            this.head = new Node(data);

        } else {
            while(tail.getNextNode() != null){
                tail = tail.getNextNode();
            }
            tail.setNextNode(new Node(data));
        }



    }

    public String removeHead(){
        Node removedHead = this.head;
        if (removedHead == null){
            return null;
        }

        this.head = removedHead.getNextNode();
        removedHead.setNextNode(null);
        return removedHead.data;
    }


    public String printList(){
        StringBuilder output = new StringBuilder("<head> ");
        Node currentNode = this.head;
        while(currentNode != null){
            output.append(currentNode.data).append(" ");
            currentNode = currentNode.getNextNode();
        }
        output.append(" <tail>");
        System.out.println(output);
        return output.toString();
    }

    public static void main(String []args) {
        // Write your code here:
        LinkedList seasons = new LinkedList();
        seasons.printList();

        seasons.addToHead("summer");
        seasons.addToHead("spring");
        seasons.printList();

        seasons.addToTail("fall");
        seasons.addToTail("winter");
        seasons.printList();

        seasons.removeHead();
        seasons.printList();
    }

}

