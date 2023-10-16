using System.Reflection;
using System.Runtime.CompilerServices;

namespace CacheService.Tests;

public class CacheTest
{
    [SetUp]
    public void Setup()
    {
    }

    [Test]
    public void Constructs()
    {
        var cache = new Cache(2);
        Assert.Multiple(() =>
        {
            Assert.That(cache.Head, Is.Null);
            Assert.That(cache.Tail, Is.Null);
            Assert.That(cache.CurrentSize, Is.EqualTo(0));
            Assert.That(cache.MaxSize, Is.EqualTo(2));
        });
    }

    [Test]
    public void Returns_Null_For_Non_Cached_Key()
    {
        var cache = new Cache(2);
        var result = cache.Get("applers");
        Assert.That(result, Is.Null);
    }

    [Test]
    public void Support_One_Cached_Value()
    {
        var cache = new Cache(3);
        cache.Put("bananas", 111);
        Assert.Multiple(() => 
        {
            Assert.That(cache.CurrentSize, Is.EqualTo(1));
            Assert.That(cache.Tail.Value, Is.EqualTo(111));
            Assert.That(cache.Head.Value, Is.EqualTo(111));
        });
    }

    [Test]
    public void Support_Two_Cached_Values()
    {
    var cache = new Cache(3);
        cache.Put("bananas", 111);
        cache.Put("apples", 222);
        Assert.Multiple(() => 
        {
            Assert.That(cache.CurrentSize, Is.EqualTo(2));
            Assert.That(cache.Tail.Value, Is.EqualTo(222));
            Assert.That(cache.Head.Value, Is.EqualTo(111));
        });
    }

    [Test]   
    public void Enforces_Max_Size_On_Set()
    {
        var cache = new Cache(3);
        cache.Put("bananas", 111);
        cache.Put("apples", 222);
        cache.Put("oranges", 333);
        cache.Put("cucumbers", 444);
        Assert.That(cache.CurrentSize, Is.EqualTo(3));        
        CollectionAssert.AreEqual(cache.ToArray(), new[]{222, 333, 444});
    }

    [Test]
    public void GetsTail()
    {
        var cache = new Cache(3);
        cache.Put("bananas", 111);
        cache.Put("apples", 222);
        cache.Put("oranges", 333);        
        cache.Get("oranges");
        CollectionAssert.AreEqual(cache.ToArray(), new[]{111, 222, 333});

    }    
    [Test]
    public void GetsHead()
    {
        var cache = new Cache(3);
        cache.Put("bananas", 111);
        cache.Put("apples", 222);
        cache.Put("oranges", 333);        
        cache.Get("bananas");
        CollectionAssert.AreEqual(cache.ToArray(), new[]{222, 333, 111});
    }

    [Test]
    public void Moves_Tail_When_Getting_Middle()
    {
        var cache = new Cache(3);
        cache.Put("bananas", 111);
        cache.Put("apples", 222);
        cache.Put("oranges", 333);        
        cache.Get("apples");
        CollectionAssert.AreEqual(cache.ToArray(), new[]{111, 333, 222});
    }

    [Test]
    public void Moves_Tail_On_Multiple_Gets()
    {
        var cache = new Cache(4);
        cache.Put("bananas", 111);
        cache.Put("apples", 222);
        cache.Put("oranges", 333);        
        cache.Put("cucumbers", 444);
        cache.Put("peaches", 555);
        cache.Get("oranges");
        cache.Get("apples");
        cache.Get("cucumbers");
        CollectionAssert.AreEqual(cache.ToArray(), new[]{555, 333, 222, 444});
    }
}

