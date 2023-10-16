namespace CacheService;

public class Node
{
    public String Key { get; }
    public int Value { get; }
    public Node? NextNode { get; set;}
    public Node? PrevNode { get; set;}

    public Node(String key, int value, Node? nextNode, Node? prevNode)
    {
        Key = key;
        Value = value;
        NextNode = nextNode;
        PrevNode = prevNode;
    }
}
