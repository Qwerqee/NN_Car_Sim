using UnityEngine;
using UnityEngine.UI;
using System.Collections;
using UnityEngine.SceneManagement;

public class MenuOptions : MonoBehaviour
{
    private int track = 0;
    private Outline[] outlines;

    public void Start ()
    {
        outlines = GetComponentsInChildren<Outline>();
    }
    
	public void MainMenu()
	{
		SceneManager.LoadScene("MenuScene");
	}

    public void StartDrivingMode()
    {
        switch (track)
        {
            case 0:
                SceneManager.LoadScene("HillTrackTraining");
                break;

            case 1:
                SceneManager.LoadScene("SnakeTrackTraining");
                break;

        }
    }

    public void StartAutonomousMode()
    {
        switch (track)
        {
            case 0:
                SceneManager.LoadScene("HillTrackAuto");
                break;

            case 1:
                SceneManager.LoadScene("SnakeTrackAuto");
                break;
        }
    }

    public void SetHillTrack()
    {
        outlines[0].enabled = true;
        outlines[1].enabled = false;
        track = 0;
    }

    public void SetSnakeTrack()
    {
        outlines[0].enabled = false;
        outlines[1].enabled = true;
        track = 1;
    }
}
