void if_while_c(int i)
{
    int s = 0;
    while (i < 10)
    {
        if (i == 5)
        {
            s += 50;
        }
        else
        {
            s += i;
        }
        i += 1;
    }
}
