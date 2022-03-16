import java.util.ArrayList;

/**
 * We will maintain the children of TreeNode as an ArrayList.
 * Using an ArrayList for the children will make adding and
 * removing children quicker and easier
 *
 */
import java.util.ArrayList;

public class TreeNode {

    public Object data;
    public ArrayList<TreeNode> children;

    public TreeNode(Object data) {
        this.data = data;
        this.children = new ArrayList<TreeNode>();
    }

    // addChild() method with parameter TreeNode child
    public void addChild(TreeNode child){
        this.children.add(child);
    }
    // addChild() method with parameter Object data
    public void addChild(Object childData){
        this.children.add(new TreeNode(childData));
    }

    public void removeChild(TreeNode childToRemove){
        if(this.children.isEmpty()){
            return;
        }else if(this.children.contains(childToRemove)){
            this.children.remove(childToRemove);
            return;

        }else{
            for (TreeNode child : this.children){
                child.removeChild(childToRemove);
            }
        }

    }

    public void removeChild(Object targetData){
        if(this.children.isEmpty()){
            return;
        }

        for (TreeNode child : this.children){
            if (child.data == targetData){
                this.children.remove(child);
            }
        }

        for (TreeNode child : this.children) {
            child.removeChild(targetData);
        }

    }

    // Define depthFirstTraversal() below
    public void depthFirstTraversal(TreeNode current) {
        System.out.print(current.data + " ");
        for (TreeNode child : current.children) {
            depthFirstTraversal(child);
        }
    }





    public static void main(String[] args) {
        TreeNode root = new TreeNode(20);
        // Add child below
        root.addChild(15);
        // Print size of root's chilren list
        System.out.print(root.children.size());
        TreeNode biggerChild = new TreeNode(30);
        root.addChild(biggerChild);
        System.out.print(root.children.size());
    }
}