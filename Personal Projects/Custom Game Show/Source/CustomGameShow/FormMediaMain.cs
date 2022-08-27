/********************************
 * Custom Game Show
 * FormMediaMain.cs
 * Created by Justin Leonard
********************************/

using System;
using System.Drawing;
using System.IO;
using System.Windows.Forms;

namespace CustomGameShow
{
    public partial class FormMediaMain : Form
    {
        /*
         * Fields
         */
        private int category, number;
        private MediaState state;

        /*
         * Types
         */
        
        public enum MediaType
        {
            ImageImage,
            ImageVideoImageImage,
            ImageVideoImageVideo,
            VideoImageImage,
            VideoImageVideo
        }

        public enum MediaState
        {
            ImageImage0,
            ImageImage1,
            ImageVideoImageImage0,
            ImageVideoImageImage1,
            ImageVideoImageImage2,
            ImageVideoImageImage3,
            ImageVideoImageVideo0,
            ImageVideoImageVideo1,
            ImageVideoImageVideo2,
            ImageVideoImageVideo3,
            VideoImageImage0,
            VideoImageImage1,
            VideoImageImage2,
            VideoImageVideo0,
            VideoImageVideo1,
            VideoImageVideo2
        }

        /*
         * Constructor
         */
        
        public FormMediaMain(int cat, int num, MediaType mt)
        {
            // Initialize
            InitializeComponent();

            // Set fields
            this.category = cat;
            this.number = num;

            // Media player settings
            this.WindowsMediaPlayerMain.stretchToFit = true;
            this.WindowsMediaPlayerMain.uiMode = "none";

            // Set media state
            switch (mt)
            {
                // Image question followed by an image answer
                case MediaType.ImageImage:
                    // Set state
                    this.state = MediaState.ImageImage0;

                    // Exit
                    break;

                // Image prompt and a video question followed by an image question and an image answer
                case MediaType.ImageVideoImageImage:
                    // Set state
                    this.state = MediaState.ImageVideoImageImage0;

                    // Exit
                    break;

                // Image prompt and a video question followed by an image question and a video answer
                case MediaType.ImageVideoImageVideo:
                    // Set state
                    this.state = MediaState.ImageVideoImageVideo0;

                    // Exit
                    break;

                // Video question followed by an image question and an image answer
                case MediaType.VideoImageImage:
                    // Set state
                    this.state = MediaState.VideoImageImage0;

                    // Exit
                    break;

                // Video question followed by an image question and a video answer
                case MediaType.VideoImageVideo:
                    // Set state
                    this.state = MediaState.VideoImageVideo0;

                    // Exit
                    break;

                // Other
                default:
                    // Exit
                    break;
            }

            // Load media
            this.LoadMediaInitial(mt);
        }

        /*
         * Form Events
         */
        
        private void FormMediaMain_FormClosing(object sender, FormClosingEventArgs e)
        {
            // Close media player
            this.WindowsMediaPlayerMain.close();
            this.WindowsMediaPlayerMain.Dispose();
        }

        private void FormMediaMain_KeyDown(object sender, KeyEventArgs e)
        {
            // Get click event
            switch (e.KeyCode)
            {
                // Custom 0
                case Keys.NumPad0:
                    // Display
                    this.DisplaySingle(FormMediaSingle.MediaName.DynamicCustom0);

                    // Exit
                    break;

                // Custom 1
                case Keys.NumPad1:
                    // Display
                    this.DisplaySingle(FormMediaSingle.MediaName.DynamicCustom1);

                    // Exit
                    break;

                // Custom 2
                case Keys.NumPad2:
                    // Display
                    this.DisplaySingle(FormMediaSingle.MediaName.DynamicCustom2);

                    // Exit
                    break;

                // Custom 3
                case Keys.NumPad3:
                    // Display
                    this.DisplaySingle(FormMediaSingle.MediaName.DynamicCustom3);

                    // Exit
                    break;

                // Custom 4
                case Keys.NumPad4:
                    // Display
                    this.DisplaySingle(FormMediaSingle.MediaName.DynamicCustom4);

                    // Exit
                    break;

                // Custom 5
                case Keys.NumPad5:
                    // Display
                    this.DisplaySingle(FormMediaSingle.MediaName.DynamicCustom5);

                    // Exit
                    break;

                // Custom 6
                case Keys.NumPad6:
                    // Display
                    this.DisplaySingle(FormMediaSingle.MediaName.DynamicCustom6);

                    // Exit
                    break;

                // Custom 7
                case Keys.NumPad7:
                    // Display
                    this.DisplaySingle(FormMediaSingle.MediaName.DynamicCustom7);

                    // Exit
                    break;

                // Custom 8
                case Keys.NumPad8:
                    // Display
                    this.DisplaySingle(FormMediaSingle.MediaName.DynamicCustom8);

                    // Exit
                    break;

                // Custom 9
                case Keys.NumPad9:
                    // Display
                    this.DisplaySingle(FormMediaSingle.MediaName.DynamicCustom9);

                    // Exit
                    break;

                // Custom 10
                case Keys.Divide:
                    // Display
                    this.DisplaySingle(FormMediaSingle.MediaName.DynamicCustom10);

                    // Exit
                    break;

                // Custom 11
                case Keys.Multiply:
                    // Display
                    this.DisplaySingle(FormMediaSingle.MediaName.DynamicCustom11);

                    // Exit
                    break;

                // Custom 12
                case Keys.Subtract:
                    // Display
                    this.DisplaySingle(FormMediaSingle.MediaName.DynamicCustom12);

                    // Exit
                    break;

                // Custom 13
                case Keys.Add:
                    // Display
                    this.DisplaySingle(FormMediaSingle.MediaName.DynamicCustom13);

                    // Exit
                    break;

                // Stop playback
                case Keys.Decimal:
                    // Stop
                    this.WindowsMediaPlayerMain.Ctlcontrols.currentPosition = Resources.MediaEndTime;

                    // Exit
                    break;

                // Other
                default:
                    // Exit
                    break;
            }
        }

        /*
         * Other Events
         */
        
        private void pictureBoxImage_Click(object sender, EventArgs e)
        {
            // Load media
            this.LoadMedia();
        }

        private void WindowsMediaPlayerMain_PlayStateChange(object sender, AxWMPLib._WMPOCXEvents_PlayStateChangeEvent e)
        {
            // Check if the play state changed to "MediaEnded"
            if (e.newState == 8)
            {
                // Load media
                this.LoadMedia();
            }
        }

        /*
         * Methods
         */
        
        private void CheckMedia()
        {
            // Check if files exist
            switch (this.state)
            {
                // ImageImage
                case MediaState.ImageImage0:
                case MediaState.ImageImage1:
                    // Check files exist
                    if (!File.Exists(Path.Combine(Path.Combine(Directory.GetCurrentDirectory(), Resources.GetMediaDirectory()), @"Questions\Question" + this.category + "_" + this.number + ".png")))
                    {
                        // Error
                        Resources.Error(Resources.ErrorCode.MissingMedia, @"Questions\Question" + this.category + "_" + this.number + ".png");
                    }
                    else if (!File.Exists(Path.Combine(Path.Combine(Directory.GetCurrentDirectory(), Resources.GetMediaDirectory()), @"Answers\Answer" + this.category + "_" + this.number + ".png")))
                    {
                        // Error
                        Resources.Error(Resources.ErrorCode.MissingMedia, @"Answers\Answer" + this.category + "_" + this.number + ".png");
                    }

                    // Exit
                    break;

                // ImageVideoImageImage
                case MediaState.ImageVideoImageImage0:
                case MediaState.ImageVideoImageImage1:
                case MediaState.ImageVideoImageImage2:
                case MediaState.ImageVideoImageImage3:
                    // Check files exist
                    if (!File.Exists(Path.Combine(Path.Combine(Directory.GetCurrentDirectory(), Resources.GetMediaDirectory()), @"Prompts\Prompt" + this.category + "_" + this.number + ".png")))
                    {
                        // Error
                        Resources.Error(Resources.ErrorCode.MissingMedia, @"Prompts\Prompt" + this.category + "_" + this.number + ".png");
                    }
                    else if (!File.Exists(Path.Combine(Path.Combine(Directory.GetCurrentDirectory(), Resources.GetMediaDirectory()), @"Questions\Question" + this.category + "_" + this.number + "a.mp4")))
                    {
                        // Error
                        Resources.Error(Resources.ErrorCode.MissingMedia, @"Questions\Question" + this.category + "_" + this.number + "a.mp4");
                    }
                    else if (!File.Exists(Path.Combine(Path.Combine(Directory.GetCurrentDirectory(), Resources.GetMediaDirectory()), @"Questions\Question" + this.category + "_" + this.number + "b.png")))
                    {
                        // Error
                        Resources.Error(Resources.ErrorCode.MissingMedia, @"Questions\Question" + this.category + "_" + this.number + "b.png");
                    }
                    else if (!File.Exists(Path.Combine(Path.Combine(Directory.GetCurrentDirectory(), Resources.GetMediaDirectory()), @"Answers\Answer" + this.category + "_" + this.number + ".png")))
                    {
                        // Error
                        Resources.Error(Resources.ErrorCode.MissingMedia, @"Answers\Answer" + this.category + "_" + this.number + ".png");
                    }

                    // Exit
                    break;

                // ImageVideoImageVideo
                case MediaState.ImageVideoImageVideo0:
                case MediaState.ImageVideoImageVideo1:
                case MediaState.ImageVideoImageVideo2:
                case MediaState.ImageVideoImageVideo3:
                    // Check files exist
                    if (!File.Exists(Path.Combine(Path.Combine(Directory.GetCurrentDirectory(), Resources.GetMediaDirectory()), @"Prompts\Prompt" + this.category + "_" + this.number + ".png")))
                    {
                        // Error
                        Resources.Error(Resources.ErrorCode.MissingMedia, @"Prompts\Prompt" + this.category + "_" + this.number + ".png");
                    }
                    else if (!File.Exists(Path.Combine(Path.Combine(Directory.GetCurrentDirectory(), Resources.GetMediaDirectory()), @"Questions\Question" + this.category + "_" + this.number + "a.mp4")))
                    {
                        // Error
                        Resources.Error(Resources.ErrorCode.MissingMedia, @"Questions\Question" + this.category + "_" + this.number + "a.mp4");
                    }
                    else if (!File.Exists(Path.Combine(Path.Combine(Directory.GetCurrentDirectory(), Resources.GetMediaDirectory()), @"Questions\Question" + this.category + "_" + this.number + "b.png")))
                    {
                        // Error
                        Resources.Error(Resources.ErrorCode.MissingMedia, @"Questions\Question" + this.category + "_" + this.number + "b.png");
                    }
                    else if (!File.Exists(Path.Combine(Path.Combine(Directory.GetCurrentDirectory(), Resources.GetMediaDirectory()), @"Answers\Answer" + this.category + "_" + this.number + ".mp4")))
                    {
                        // Error
                        Resources.Error(Resources.ErrorCode.MissingMedia, @"Answers\Answer" + this.category + "_" + this.number + ".mp4");
                    }

                    // Exit
                    break;

                // VideoImageImage
                case MediaState.VideoImageImage0:
                case MediaState.VideoImageImage1:
                case MediaState.VideoImageImage2:
                    // Check files exist
                    if (!File.Exists(Path.Combine(Path.Combine(Directory.GetCurrentDirectory(), Resources.GetMediaDirectory()), @"Questions\Question" + this.category + "_" + this.number + "a.mp4")))
                    {
                        // Error
                        Resources.Error(Resources.ErrorCode.MissingMedia, @"Questions\Question" + this.category + "_" + this.number + "a.mp4");
                    }
                    else if (!File.Exists(Path.Combine(Path.Combine(Directory.GetCurrentDirectory(), Resources.GetMediaDirectory()), @"Questions\Question" + this.category + "_" + this.number + "b.png")))
                    {
                        // Error
                        Resources.Error(Resources.ErrorCode.MissingMedia, @"Questions\Question" + this.category + "_" + this.number + "b.png");
                    }
                    else if (!File.Exists(Path.Combine(Path.Combine(Directory.GetCurrentDirectory(), Resources.GetMediaDirectory()), @"Answers\Answer" + this.category + "_" + this.number + ".png")))
                    {
                        // Error
                        Resources.Error(Resources.ErrorCode.MissingMedia, @"Answers\Answer" + this.category + "_" + this.number + ".png");
                    }

                    // Exit
                    break;

                // VideoImageVideo
                case MediaState.VideoImageVideo0:
                case MediaState.VideoImageVideo1:
                case MediaState.VideoImageVideo2:
                    // Check files exist
                    if (!File.Exists(Path.Combine(Path.Combine(Directory.GetCurrentDirectory(), Resources.GetMediaDirectory()), @"Questions\Question" + this.category + "_" + this.number + "a.mp4")))
                    {
                        // Error
                        Resources.Error(Resources.ErrorCode.MissingMedia, @"Questions\Question" + this.category + "_" + this.number + "a.mp4");
                    }
                    else if (!File.Exists(Path.Combine(Path.Combine(Directory.GetCurrentDirectory(), Resources.GetMediaDirectory()), @"Questions\Question" + this.category + "_" + this.number + "b.png")))
                    {
                        // Error
                        Resources.Error(Resources.ErrorCode.MissingMedia, @"Questions\Question" + this.category + "_" + this.number + "b.png");
                    }
                    else if (!File.Exists(Path.Combine(Path.Combine(Directory.GetCurrentDirectory(), Resources.GetMediaDirectory()), @"Answers\Answer" + this.category + "_" + this.number + ".mp4")))
                    {
                        // Error
                        Resources.Error(Resources.ErrorCode.MissingMedia, @"Answers\Answer" + this.category + "_" + this.number + ".mp4");
                    }

                    // Exit
                    break;

                // Other
                default:
                    // Exit
                    break;
            }
        }

        private void LoadMedia()
        {
            // Check media
            this.CheckMedia();

            // Check media state
            switch (this.state)
            {
                // ImageImage0
                case MediaState.ImageImage0:
                    // Change state
                    this.state = MediaState.ImageImage1;

                    // Components
                    this.pictureBoxImage.Enabled = true;
                    this.pictureBoxImage.Visible = true;
                    this.WindowsMediaPlayerMain.Visible = false;

                    // Show image
                    this.pictureBoxImage.Image = Image.FromFile(Path.Combine(Path.Combine(Directory.GetCurrentDirectory(), Resources.GetMediaDirectory()), @"Answers\Answer" + this.category + "_" + this.number + ".png"));

                    // Exit
                    break;

                // ImageImage1
                case MediaState.ImageImage1:
                    // Exit form
                    this.Close();

                    // Exit
                    break;

                // ImageVideoImageImage0
                case MediaState.ImageVideoImageImage0:
                    // Change state
                    this.state = MediaState.ImageVideoImageImage1;

                    // Components
                    this.pictureBoxImage.Enabled = false;
                    this.pictureBoxImage.Visible = false;
                    this.WindowsMediaPlayerMain.Visible = true;

                    // Play video
                    this.WindowsMediaPlayerMain.URL = Path.Combine(Path.Combine(Directory.GetCurrentDirectory(), Resources.GetMediaDirectory()), @"Questions\Question" + this.category + "_" + this.number + "a.mp4");

                    // Exit
                    break;

                // ImageVideoImageImage1
                case MediaState.ImageVideoImageImage1:
                    // Change state
                    this.state = MediaState.ImageVideoImageImage2;

                    // Components
                    this.pictureBoxImage.Enabled = true;
                    this.pictureBoxImage.Visible = true;
                    this.WindowsMediaPlayerMain.Visible = false;

                    // Show image
                    this.pictureBoxImage.Image = Image.FromFile(Path.Combine(Path.Combine(Directory.GetCurrentDirectory(), Resources.GetMediaDirectory()), @"Questions\Question" + this.category + "_" + this.number + "b.png"));

                    // Exit
                    break;

                // ImageVideoImageImage2
                case MediaState.ImageVideoImageImage2:
                    // Change state
                    this.state = MediaState.ImageVideoImageImage3;

                    // Components
                    this.pictureBoxImage.Enabled = true;
                    this.pictureBoxImage.Visible = true;
                    this.WindowsMediaPlayerMain.Visible = false;

                    // Show image
                    this.pictureBoxImage.Image = Image.FromFile(Path.Combine(Path.Combine(Directory.GetCurrentDirectory(), Resources.GetMediaDirectory()), @"Answers\Answer" + this.category + "_" + this.number + ".png"));

                    // Exit
                    break;

                // ImageVideoImageImage3
                case MediaState.ImageVideoImageImage3:
                    // Exit form
                    this.Close();

                    // Exit
                    break;

                // ImageVideoImageVideo0
                case MediaState.ImageVideoImageVideo0:
                    // Change state
                    this.state = MediaState.ImageVideoImageVideo1;

                    // Components
                    this.pictureBoxImage.Enabled = false;
                    this.pictureBoxImage.Visible = false;
                    this.WindowsMediaPlayerMain.Visible = true;

                    // Play video
                    this.WindowsMediaPlayerMain.URL = Path.Combine(Path.Combine(Directory.GetCurrentDirectory(), Resources.GetMediaDirectory()), @"Questions\Question" + this.category + "_" + this.number + "a.mp4");

                    // Exit
                    break;

                // ImageVideoImageVideo1
                case MediaState.ImageVideoImageVideo1:
                    // Change state
                    this.state = MediaState.ImageVideoImageVideo2;

                    // Components
                    this.pictureBoxImage.Enabled = true;
                    this.pictureBoxImage.Visible = true;
                    this.WindowsMediaPlayerMain.Visible = false;

                    // Show image
                    this.pictureBoxImage.Image = Image.FromFile(Path.Combine(Path.Combine(Directory.GetCurrentDirectory(), Resources.GetMediaDirectory()), @"Questions\Question" + this.category + "_" + this.number + "b.png"));

                    // Exit
                    break;

                // ImageVideoImageVideo2
                case MediaState.ImageVideoImageVideo2:
                    // Change state
                    this.state = MediaState.ImageVideoImageVideo3;

                    // Components
                    this.pictureBoxImage.Enabled = false;
                    this.pictureBoxImage.Visible = false;
                    this.WindowsMediaPlayerMain.Visible = true;

                    // Play video
                    this.WindowsMediaPlayerMain.URL = Path.Combine(Path.Combine(Directory.GetCurrentDirectory(), Resources.GetMediaDirectory()), @"Answers\Answer" + this.category + "_" + this.number + ".mp4");

                    // Exit
                    break;

                // ImageVideoImageVideo3
                case MediaState.ImageVideoImageVideo3:
                    // Exit form
                    this.Close();

                    // Exit
                    break;

                // VideoImageImage0
                case MediaState.VideoImageImage0:
                    // Change state
                    this.state = MediaState.VideoImageImage1;

                    // Components
                    this.pictureBoxImage.Enabled = true;
                    this.pictureBoxImage.Visible = true;
                    this.WindowsMediaPlayerMain.Visible = false;

                    // Show image
                    this.pictureBoxImage.Image = Image.FromFile(Path.Combine(Path.Combine(Directory.GetCurrentDirectory(), Resources.GetMediaDirectory()), @"Questions\Question" + this.category + "_" + this.number + "b.png"));

                    // Exit
                    break;

                // VideoImageImage1
                case MediaState.VideoImageImage1:
                    // Change state
                    this.state = MediaState.VideoImageImage2;

                    // Components
                    this.pictureBoxImage.Enabled = true;
                    this.pictureBoxImage.Visible = true;
                    this.WindowsMediaPlayerMain.Visible = false;

                    // Show image
                    this.pictureBoxImage.Image = Image.FromFile(Path.Combine(Path.Combine(Directory.GetCurrentDirectory(), Resources.GetMediaDirectory()), @"Answers\Answer" + this.category + "_" + this.number + ".png"));

                    // Exit
                    break;

                // VideoImageImage2
                case MediaState.VideoImageImage2:
                    // Exit form
                    this.Close();

                    // Exit
                    break;

                // VideoImageVideo0
                case MediaState.VideoImageVideo0:
                    // Change state
                    this.state = MediaState.VideoImageVideo1;

                    // Components
                    this.pictureBoxImage.Enabled = true;
                    this.pictureBoxImage.Visible = true;
                    this.WindowsMediaPlayerMain.Visible = false;

                    // Show image
                    this.pictureBoxImage.Image = Image.FromFile(Path.Combine(Path.Combine(Directory.GetCurrentDirectory(), Resources.GetMediaDirectory()), @"Questions\Question" + this.category + "_" + this.number + "b.png"));

                    // Exit
                    break;

                // VideoImageVideo1
                case MediaState.VideoImageVideo1:
                    // Change state
                    this.state = MediaState.VideoImageVideo2;

                    // Components
                    this.pictureBoxImage.Enabled = false;
                    this.pictureBoxImage.Visible = false;
                    this.WindowsMediaPlayerMain.Visible = true;

                    // Play video
                    this.WindowsMediaPlayerMain.URL = Path.Combine(Path.Combine(Directory.GetCurrentDirectory(), Resources.GetMediaDirectory()), @"Answers\Answer" + this.category + "_" + this.number + ".mp4");

                    // Exit
                    break;

                // VideoImageVideo2
                case MediaState.VideoImageVideo2:
                    // Exit form
                    this.Close();

                    // Exit
                    break;

                // Other
                default:
                    // Exit
                    break;
            }
        }

        private void LoadMediaInitial(MediaType mt)
        {
            // Check media
            this.CheckMedia();

            // Set media state
            switch (mt)
            {
                // Image question followed by an image answer
                case MediaType.ImageImage:
                    // Components
                    this.pictureBoxImage.Enabled = true;
                    this.pictureBoxImage.Visible = true;
                    this.WindowsMediaPlayerMain.Visible = false;

                    // Show image
                    this.pictureBoxImage.Image = Image.FromFile(Path.Combine(Path.Combine(Directory.GetCurrentDirectory(), Resources.GetMediaDirectory()), @"Questions\Question" + this.category + "_" + this.number + ".png"));

                    // Exit
                    break;

                // Image prompt and a video question followed by an image question and an image answer
                case MediaType.ImageVideoImageImage:
                    // Components
                    this.pictureBoxImage.Enabled = true;
                    this.pictureBoxImage.Visible = true;
                    this.WindowsMediaPlayerMain.Visible = false;

                    // Show image
                    this.pictureBoxImage.Image = Image.FromFile(Path.Combine(Path.Combine(Directory.GetCurrentDirectory(), Resources.GetMediaDirectory()), @"Prompts\Prompt" + this.category + "_" + this.number + ".png"));

                    // Exit
                    break;

                // Image prompt and a video question followed by an image question and a video answer
                case MediaType.ImageVideoImageVideo:
                    // Components
                    this.pictureBoxImage.Enabled = true;
                    this.pictureBoxImage.Visible = true;
                    this.WindowsMediaPlayerMain.Visible = false;

                    // Show image
                    this.pictureBoxImage.Image = Image.FromFile(Path.Combine(Path.Combine(Directory.GetCurrentDirectory(), Resources.GetMediaDirectory()), @"Prompts\Prompt" + this.category + "_" + this.number + ".png"));

                    // Exit
                    break;

                // Video question followed by an image question and an image answer
                case MediaType.VideoImageImage:
                    // Components
                    this.pictureBoxImage.Enabled = false;
                    this.pictureBoxImage.Visible = false;
                    this.WindowsMediaPlayerMain.Visible = true;

                    // Play video
                    this.WindowsMediaPlayerMain.URL = Path.Combine(Path.Combine(Directory.GetCurrentDirectory(), Resources.GetMediaDirectory()), @"Questions\Question" + this.category + "_" + this.number + "a.mp4");

                    // Exit
                    break;

                // Video question followed by an image question and a video answer
                case MediaType.VideoImageVideo:
                    // Components
                    this.pictureBoxImage.Enabled = false;
                    this.pictureBoxImage.Visible = false;
                    this.WindowsMediaPlayerMain.Visible = true;

                    // Play video
                    this.WindowsMediaPlayerMain.URL = Path.Combine(Path.Combine(Directory.GetCurrentDirectory(), Resources.GetMediaDirectory()), @"Questions\Question" + this.category + "_" + this.number + "a.mp4");

                    // Exit
                    break;

                // Other
                default:
                    // Exit
                    break;
            }
        }

        private void DisplaySingle(FormMediaSingle.MediaName mn)
        {
            // Variables
            Form tempForm = new FormMediaSingle(mn);

            // Show form
            var result = tempForm.ShowDialog();
        }
    }
}
