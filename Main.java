import java.util.*;
import java.io.*;

class Main
{
	static int maximalRectangle(int row, int col, int A[][])
	{
		// Tính diện tích dòng đầu
		int result = maximalRectangleInHistogram(row,col,A[0]);

		// vòng lặp dùng để chạy tất cả và so sánh 
		for (int i = 1; i < row; i++) 
        { 
       
            for (int j = 0; j< col; j++)
                // if A[i][j] = 1 thì A[i][j] = A[i][j] + A[i -1][j] 
                if (A[i][j] == 1) 
                	A[i][j] += A[i - 1][j]; 
       		// so sánh và cập nhật cái area hiện tại và cái tiếp theo 
            result = Math.max(result, maximalRectangleInHistogram(row,col,A[i])); 
        } 
       
        return result;

	}


	static int maximalRectangleInHistogram(int rows,int col,int row[]) 
    { 
        // Tạo Stack integer 
        Stack<Integer> result = new Stack<Integer>(); 
       	// Phần tử top của Stack 
        int top_val;     
       	// Diện tích tối đa hiện tại, theo hàng(dòng)
        int max_area = 0; 
       	// area hiện tại
        int area = 0;    
       
        // tạo vòng lặp để chạy 
        int i = 0; 
        while (i < col) 
        { 
            // if result is empty and the top is smaller than row[i] append(push) result
            if (result.empty() || row[result.peek()] <= row[i]) 
                result.push(i++); 
       
            else
            { 
                
                top_val = row[result.peek()]; // lấy phần tử đầu (Top)
                result.pop(); // pop phần tử đầu (Top)
                area = top_val * i; //tính diện tích  với i là cột
       
                if (!result.empty()) // if result is empty then 
                    area = top_val * (i - result.peek() - 1 ); // col is i - result.peek() -1
                max_area = Math.max(area, max_area); // compare và gán cái lớn nhất
            } 
        } 
       
        // Clean the stack. 
        while (!result.empty()) 
        { 
            top_val = row[result.peek()]; 
            result.pop(); 
            area = top_val * i; 
            if (!result.empty()) 
                area = top_val * (i - result.peek() - 1 ); 
       
            max_area = Math.max(area, max_area); 
        } 

        return max_area; 
    }

    public static void main (String[] args) throws Exception
    {
        File file = new File(args[0]); 
        int i = 0;
  
        BufferedReader br = new BufferedReader(new FileReader(file)); 
        String st; // biến dùng để gán line
        
        int rowCol = Integer.parseInt(br.readLine()); // number of row and col 

        int array[][] = new int[rowCol][rowCol]; // create array
        // read file, read line
        while ((st = br.readLine()) != null){
            String[] a = st.split(" "); // split String. (number 0 1 1 ...)
            for(int j =0 ; j< rowCol ; j++){
                array[i][j] = Integer.parseInt(a[j]); // append number of array
            }
            i++; // i = i+1 
        }
       
        String str = maximalRectangle(rowCol,rowCol,array)+ "";// convert the number we want to print to String
        BufferedWriter writer = new BufferedWriter(new FileWriter(args[1])); // write file
        writer.write(str);
     
        writer.close();


    }

}