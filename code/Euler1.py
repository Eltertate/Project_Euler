int count;
int answer = 0;

for (count = 1; count < 1000; count++)
{
    if (count % 3 == 0 || count % 5 == 0)
    {
        answer += count;
    }
}
Console.WriteLine(answer);
