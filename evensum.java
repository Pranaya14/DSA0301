import java.util.*;
class evensum{
public static void main(String[] args)
{
int sum=0;
Scanner s = new Scanner(System.in);
System.out.println("enter the number:");
int n = s.nextInt();
int f[] = new int[2 * n + 1];
f[0] = 0;
f[1] = 1;
for(int i=2 ; i<=2*n ; i++)
{
f[i] = f[i-1]+f[i-2];
if(i%2==0)
{
sum+=f[i];
}
}
System.out.println("even sum :"+sum);
}
}

