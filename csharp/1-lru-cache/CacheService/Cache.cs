using System.Security.Cryptography;

namespace CacheService;

public class Cache
{
    public int MaxSize { get; private set; }
    private Dictionary<string, Node> LookupTable;
    public int CurrentSize { get; private set; }
    public Node? Head { get; private set; }
    public Node? Tail { get; private set;}

    public Cache(int maxSize)
    {   
        Tail = null;     
        Head = null;
        CurrentSize = 0;
        MaxSize = maxSize;        
        LookupTable = new();        
    }

    public int? Get(string key) 
    {
        
        if (!this.LookupTable.ContainsKey(key))
        {
            return null;
        }

        Node result = this.LookupTable[key];

        if (Tail == result)
        {
            return result.Value;
        }

        if (null == result.PrevNode)
        {
            Head = result.NextNode;
            Head.PrevNode = null;
        }        

        Tail.NextNode = result;
        result.NextNode = null;
        result.PrevNode = Tail;
        Tail = result;

        return result.Value;
    }

    public void Put(string key, int val) {        

        CurrentSize += 1;
        if (CurrentSize > MaxSize) {
            LookupTable.Remove(Head.Key);
            Head = Head.NextNode;
            Head.PrevNode = null;
            CurrentSize -= 1;
        }

        Node newNode = new Node(key, val, null, Tail);

        if (null == Tail) 
        {
            Head = newNode;
        } 
        else 
        {
            Tail.NextNode = newNode;
        }        
        Tail = newNode;
        LookupTable.Add(key, newNode);
    }

    public int[] ToArray()
    {       
        var a = new List<int>();
        var current = Head;
        while (null != current)
        {
            a.Add(current.Value);
            current = current.NextNode;
        }
        return a.ToArray();
    }
}
