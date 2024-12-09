// in this unity how many different scrips are there, all are classes.and we can make the objects from it.
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class BallMovement : MonoBehaviour
{

    public UDPReceive udpReceive;
    // Start is called before the first frame update

    // for sound when collide
    public AudioSource audioPlayer;
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        string data=udpReceive.data;
        // we got the data in terms of the tuple and with the  bracket , so we have to remove that bracket.
        data=data.Remove(0,1);  // here starting from index -0 remove 1 - so from this opening bracket removed.
        data=data.Remove(data.Length-1,1); //removing the last bracket.

        // split that 3 values x y and area by ','
        string[] info=data.Split(',');
        // here this all values convert into the float , because ball movement in any direction can be in floating point value
        //here, divide the values by the specific number because , the movement of any object in unity is very less or in points(0.1,0.2,0.3.)
        // by dividing them reach in the range.
        float x=5-float.Parse(info[0])/100;
        float y=float.Parse(info[1])/100;
        float z=-10+float.Parse(info[2])/1000;

        //we have to move the ball by the values of the x,y,z which values are come from the udpReceiver and values originate from pycharm
        gameObject.transform.localPosition = new Vector3(x,y,z);

        
    }

    public void OnCollisionEnter2D(Collision2D collision)
{
    if (collision.gameObject.tag == "CollisionTag")
    {
        Debug.Log("Collision detected with 'CollisionTag'");
        audioPlayer.Play();
        Debug.Log("Audio played");
    }
}

}