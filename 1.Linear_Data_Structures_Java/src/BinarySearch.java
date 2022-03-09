import java.util.Arrays;

public class BinarySearch {
    public static int search(int[] arr, int target) {
        // Add left and right variables below
        int left = 0;
        int right = arr.length;
        // Add mid calculation below
        while (left<right) {
            int mid = Math.floorDiv(right + left, 2);
            int midValue = arr[mid];
            if (midValue == target) {
                return mid;
            } else if (target<midValue){
                right = mid;
            } else {
                left = mid+1;
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        int[] searchable = {1, 2, 7, 8, 22, 28, 41, 58, 67, 71, 94};
        int target = 7;


        System.out.println(search(searchable, target));
    }

}