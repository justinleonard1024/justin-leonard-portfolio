/********************************
 * Custom Game Show
 * FormGameBoard.cs
 * Created by Justin Leonard
********************************/

using System;
using System.Configuration;
using System.Drawing;
using System.IO;
using System.Windows.Forms;

namespace CustomGameShow
{
    public partial class FormGameBoard : Form
    {
        /*
         * Fields
         */
        public int score0, score1, score2, scoreUndo, counter, round;
        public int lastPressedCategory, lastPressedNumber;
        public string logOriginal;
        public FormMediaMain.MediaType lastPressedMediaType;
        public bool[,] logMedia;

        /*
         * Constructor
         */
        
        public FormGameBoard()
        {
            // Initialize
            InitializeComponent();

            // Set fields
            this.score0 = 0;
            this.score1 = 0;
            this.score2 = 0;
            this.scoreUndo = -1;
            this.counter = 0;
            this.round = 1;
            this.lastPressedCategory = -1;
            this.lastPressedNumber = -1;
            this.logOriginal = "";
            this.lastPressedMediaType = FormMediaMain.MediaType.ImageImage;
            this.logMedia = new bool[10, 12];

            // Default log
            this.DefaultLog();

            // Update Log
            this.UpdateLog();

            // Load settings
            this.LoadSettings();

            // Load media
            this.LoadMedia();
        }

        /*
         * Form Events
         */
        
        private void FormGameBoard_Shown(object sender, EventArgs e)
        {
            // Display initial
            this.DisplayInitial();

            // Show game board
            this.Opacity = 100;
        }

        private void FormGameBoard_FormClosing(object sender, FormClosingEventArgs e)
        {
            // Variables
            DialogResult result;

            // Open message box
            result = MessageBox.Show("Are you sure you want to close the application?", "Close Application", MessageBoxButtons.YesNo, MessageBoxIcon.Question);

            // Check result
            if (result == DialogResult.No)
            {
                // Cancel close
                e.Cancel = true;
            }
        }

        private void FormGameBoard_FormClosed(object sender, FormClosedEventArgs e)
        {
            // Exit application
            Application.Exit();
        }

        private void FormGameBoard_KeyDown(object sender, KeyEventArgs e)
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

                // Other
                default:
                    // Exit
                    break;
            }
        }

        /*
         * Button Events
         */
        
        private void buttonMain_Click(object sender, EventArgs e)
        {
            // Variables
            int category, number;
            string btnName, mediaTypeRaw;
            FormMediaMain.MediaType mediaType = FormMediaMain.MediaType.ImageImage;
            Button tempButton = (sender as Button);
            var settings = ConfigurationManager.AppSettings;
            string[] vals;

            // Get button name
            btnName = tempButton.Name;

            // Get values
            vals = btnName.Replace("buttonMain", string.Empty).Split('_');
            category = Int32.Parse(vals[0]);
            number = Int32.Parse(vals[1]);

            // Set media type
            mediaTypeRaw = settings["mediaType" + category + "_" + number];

            switch (mediaTypeRaw)
            {
                case "ImageImage":
                    mediaType = FormMediaMain.MediaType.ImageImage;
                    break;
                case "ImageVideoImageImage":
                    mediaType = FormMediaMain.MediaType.ImageVideoImageImage;
                    break;
                case "ImageVideoImageVideo":
                    mediaType = FormMediaMain.MediaType.ImageVideoImageVideo;
                    break;
                case "VideoImageImage":
                    mediaType = FormMediaMain.MediaType.VideoImageImage;
                    break;
                case "VideoImageVideo":
                    mediaType = FormMediaMain.MediaType.VideoImageVideo;
                    break;
            }

            // Disable main button
            tempButton.Enabled = false;
            tempButton.Visible = false;

            // Add to counter
            this.counter++;

            // Display media
            this.DisplayMedia(category, number, mediaType);

            // Check round
            this.CheckRound();

            // Set last pressed
            this.lastPressedCategory = category;
            this.lastPressedNumber = number;
            this.lastPressedMediaType = mediaType;

            // Set media log
            this.logMedia[category, number] = true;

            // Update Log
            this.UpdateLog();
        }

        private void buttonScoreAdd_Click(object sender, EventArgs e)
        {
            // Display score add
            this.DisplayScoreAdd();
        }

        private void buttonScoreView_Click(object sender, EventArgs e)
        {
            // Display score view
            this.DisplayScoreView();
        }

        private void buttonMedia_Click(object sender, EventArgs e)
        {
            // Display media
            this.DisplayMedia();
        }

        private void buttonEdit_Click(object sender, EventArgs e)
        {
            // Display edit
            this.DisplayEdit();
        }

        private void buttonReplay_Click(object sender, EventArgs e)
        {
            // Check last pressed
            if(this.lastPressedCategory != -1 && this.lastPressedNumber != -1)
            {
                // Display media
                this.DisplayMedia(this.lastPressedCategory, this.lastPressedNumber, this.lastPressedMediaType);
            }
            else
            {
                // Show message
                MessageBox.Show("No button has been pressed yet", "Replay", MessageBoxButtons.OK);
            }
        }

        private void buttonInfo_Click(object sender, EventArgs e)
        {
            // Display info
            this.DisplayInfo();
        }

        private void buttonFinaleWinner0_Click(object sender, EventArgs e)
        {
            // Variables
            var settings = ConfigurationManager.AppSettings;

            // Display winner
            this.DisplaySingle(FormMediaSingle.MediaName.FinaleWinner0);
        }

        private void buttonFinaleWinner1_Click(object sender, EventArgs e)
        {
            // Variables
            var settings = ConfigurationManager.AppSettings;

            // Display winner
            this.DisplaySingle(FormMediaSingle.MediaName.FinaleWinner1);
        }

        private void buttonFinaleWinner2_Click(object sender, EventArgs e)
        {
            // Variables
            var settings = ConfigurationManager.AppSettings;

            // Display winner
            this.DisplaySingle(FormMediaSingle.MediaName.FinaleWinner2);
        }

        private void buttonFinaleWinnerFinal_Click(object sender, EventArgs e)
        {
            // Variables
            var settings = ConfigurationManager.AppSettings;

            // Display winner
            this.DisplaySingle(FormMediaSingle.MediaName.FinaleWinnerFinal);
        }

        private void buttonClose_Click(object sender, EventArgs e)
        {
            // Close application
            this.Close();
        }

        /*
         * Methods
         */
        
        private void CheckMedia()
        {
            // Variables
            var settings = ConfigurationManager.AppSettings;

            // Check questions, answers and prompts
            for (int i = 0; i < 10; i++)
            {
                for (int j = 0; j < 12; j++)
                {
                    // Check each question, answer and prompt
                    switch (settings["mediaType" + i + "_" + j])
                    {
                        // Image question followed by an image answer
                        case "ImageImage":
                            // Check files exist
                            if (!File.Exists(Path.Combine(Path.Combine(Directory.GetCurrentDirectory(), Resources.GetMediaDirectory()), @"Questions\Question" + i + "_" + j + ".png")))
                            {
                                // Error
                                Resources.Error(Resources.ErrorCode.MissingMedia, @"Questions\Question" + i + "_" + j + ".png");
                            }
                            else if (!File.Exists(Path.Combine(Path.Combine(Directory.GetCurrentDirectory(), Resources.GetMediaDirectory()), @"Answers\Answer" + i + "_" + j + ".png")))
                            {
                                // Error
                                Resources.Error(Resources.ErrorCode.MissingMedia, @"Answers\Answer" + i + "_" + j + ".png");
                            }

                            // Exit
                            break;

                        // Image prompt and a video question followed by an image question and an image answer
                        case "ImageVideoImageImage":
                            // Check files exist
                            if (!File.Exists(Path.Combine(Path.Combine(Directory.GetCurrentDirectory(), Resources.GetMediaDirectory()), @"Prompts\Prompt" + i + "_" + j + ".png")))
                            {
                                // Error
                                Resources.Error(Resources.ErrorCode.MissingMedia, @"Prompts\Prompt" + i + "_" + j + ".png");
                            }
                            else if (!File.Exists(Path.Combine(Path.Combine(Directory.GetCurrentDirectory(), Resources.GetMediaDirectory()), @"Questions\Question" + i + "_" + j + "a.mp4")))
                            {
                                // Error
                                Resources.Error(Resources.ErrorCode.MissingMedia, @"Questions\Question" + i + "_" + j + "a.mp4");
                            }
                            else if (!File.Exists(Path.Combine(Path.Combine(Directory.GetCurrentDirectory(), Resources.GetMediaDirectory()), @"Questions\Question" + i + "_" + j + "b.png")))
                            {
                                // Error
                                Resources.Error(Resources.ErrorCode.MissingMedia, @"Questions\Question" + i + "_" + j + "b.png");
                            }
                            else if (!File.Exists(Path.Combine(Path.Combine(Directory.GetCurrentDirectory(), Resources.GetMediaDirectory()), @"Answers\Answer" + i + "_" + j + ".png")))
                            {
                                // Error
                                Resources.Error(Resources.ErrorCode.MissingMedia, @"Answers\Answer" + i + "_" + j + ".png");
                            }

                            // Exit
                            break;

                        // Image prompt and a video question followed by an image question and a video answer
                        case "ImageVideoImageVideo":
                            // Check files exist
                            if (!File.Exists(Path.Combine(Path.Combine(Directory.GetCurrentDirectory(), Resources.GetMediaDirectory()), @"Prompts\Prompt" + i + "_" + j + ".png")))
                            {
                                // Error
                                Resources.Error(Resources.ErrorCode.MissingMedia, @"Prompts\Prompt" + i + "_" + j + ".png");
                            }
                            else if (!File.Exists(Path.Combine(Path.Combine(Directory.GetCurrentDirectory(), Resources.GetMediaDirectory()), @"Questions\Question" + i + "_" + j + "a.mp4")))
                            {
                                // Error
                                Resources.Error(Resources.ErrorCode.MissingMedia, @"Questions\Question" + i + "_" + j + "a.mp4");
                            }
                            else if (!File.Exists(Path.Combine(Path.Combine(Directory.GetCurrentDirectory(), Resources.GetMediaDirectory()), @"Questions\Question" + i + "_" + j + "b.png")))
                            {
                                // Error
                                Resources.Error(Resources.ErrorCode.MissingMedia, @"Questions\Question" + i + "_" + j + "b.png");
                            }
                            else if (!File.Exists(Path.Combine(Path.Combine(Directory.GetCurrentDirectory(), Resources.GetMediaDirectory()), @"Answers\Answer" + i + "_" + j + ".mp4")))
                            {
                                // Error
                                Resources.Error(Resources.ErrorCode.MissingMedia, @"Answers\Answer" + i + "_" + j + ".mp4");
                            }

                            // Exit
                            break;

                        // Video question followed by an image question and an image answer
                        case "VideoImageImage":
                            // Check files exist
                            if (!File.Exists(Path.Combine(Path.Combine(Directory.GetCurrentDirectory(), Resources.GetMediaDirectory()), @"Questions\Question" + i + "_" + j + "a.mp4")))
                            {
                                // Error
                                Resources.Error(Resources.ErrorCode.MissingMedia, @"Questions\Question" + i + "_" + j + "a.mp4");
                            }
                            else if (!File.Exists(Path.Combine(Path.Combine(Directory.GetCurrentDirectory(), Resources.GetMediaDirectory()), @"Questions\Question" + i + "_" + j + "b.png")))
                            {
                                // Error
                                Resources.Error(Resources.ErrorCode.MissingMedia, @"Questions\Question" + i + "_" + j + "b.png");
                            }
                            else if (!File.Exists(Path.Combine(Path.Combine(Directory.GetCurrentDirectory(), Resources.GetMediaDirectory()), @"Answers\Answer" + i + "_" + j + ".png")))
                            {
                                // Error
                                Resources.Error(Resources.ErrorCode.MissingMedia, @"Answers\Answer" + i + "_" + j + ".png");
                            }

                            // Exit
                            break;

                        // Video question followed by an image question and a video answer
                        case "VideoImageVideo":
                            // Check files exist
                            if (!File.Exists(Path.Combine(Path.Combine(Directory.GetCurrentDirectory(), Resources.GetMediaDirectory()), @"Questions\Question" + i + "_" + j + "a.mp4")))
                            {
                                // Error
                                Resources.Error(Resources.ErrorCode.MissingMedia, @"Questions\Question" + i + "_" + j + "a.mp4");
                            }
                            else if (!File.Exists(Path.Combine(Path.Combine(Directory.GetCurrentDirectory(), Resources.GetMediaDirectory()), @"Questions\Question" + i + "_" + j + "b.png")))
                            {
                                // Error
                                Resources.Error(Resources.ErrorCode.MissingMedia, @"Questions\Question" + i + "_" + j + "b.png");
                            }
                            else if (!File.Exists(Path.Combine(Path.Combine(Directory.GetCurrentDirectory(), Resources.GetMediaDirectory()), @"Answers\Answer" + i + "_" + j + ".mp4")))
                            {
                                // Error
                                Resources.Error(Resources.ErrorCode.MissingMedia, @"Answers\Answer" + i + "_" + j + ".mp4");
                            }

                            // Exit
                            break;

                        // Other
                        default:
                            // Exit
                            break;
                    }
                }
            }

            // Check custom
            for (int i = 0; i < 14; i++)
            {
                // Check files exist
                if (!File.Exists(Path.Combine(Path.Combine(Directory.GetCurrentDirectory(), Resources.GetMediaDirectory()), @"Dynamic\Custom" + i + ".mp4")))
                {
                    // Error
                    Resources.Error(Resources.ErrorCode.MissingMedia, @"Dynamic\Custom" + i + ".mp4");
                }
            }

            // Check finale winner
            for (int i = 0; i < 3; i++)
            {
                // Check files exist
                if (!File.Exists(Path.Combine(Path.Combine(Directory.GetCurrentDirectory(), Resources.GetMediaDirectory()), @"Finale\Winner" + i + ".mp4")))
                {
                    // Error
                    Resources.Error(Resources.ErrorCode.MissingMedia, @"Finale\Winner" + i + ".mp4");
                }
            }

            // Check files exist
            if (!File.Exists(Path.Combine(Path.Combine(Directory.GetCurrentDirectory(), Resources.GetMediaDirectory()), @"Finale\WinnerFinal.mp4")))
            {
                // Error
                Resources.Error(Resources.ErrorCode.MissingMedia, @"Finale\WinnerFinal.mp4");
            }

            // Check category
            for (int i = 0; i < 10; i++)
            {
                // Check files exist
                if (!File.Exists(Path.Combine(Path.Combine(Directory.GetCurrentDirectory(), Resources.GetMediaDirectory()), @"GameBoard\Category" + i + ".png")))
                {
                    // Error
                    Resources.Error(Resources.ErrorCode.MissingMedia, @"GameBoard\Category" + i + ".png");
                }
            }

            // Check rounds
            for (int i = 0; i < 3; i++)
            {
                // Check files exist
                if (!File.Exists(Path.Combine(Path.Combine(Directory.GetCurrentDirectory(), Resources.GetMediaDirectory()), @"GameBoard\Round" + i + ".png")))
                {
                    // Error
                    Resources.Error(Resources.ErrorCode.MissingMedia, @"GameBoard\Round" + i + ".png");
                }
            }

            // Check other
            if (!File.Exists(Path.Combine(Path.Combine(Directory.GetCurrentDirectory(), Resources.GetMediaDirectory()), @"Finale\Background.png")))
            {
                // Error
                Resources.Error(Resources.ErrorCode.MissingMedia, @"Finale\Background.png");
            }
            else if (!File.Exists(Path.Combine(Path.Combine(Directory.GetCurrentDirectory(), Resources.GetMediaDirectory()), @"Finale\Title.png")))
            {
                // Error
                Resources.Error(Resources.ErrorCode.MissingMedia, @"Finale\Title.png");
            }
            else if (!File.Exists(Path.Combine(Path.Combine(Directory.GetCurrentDirectory(), Resources.GetMediaDirectory()), @"GameBoard\Final.png")))
            {
                // Error
                Resources.Error(Resources.ErrorCode.MissingMedia, @"GameBoard\Final.png");
            }
            else if (!File.Exists(Path.Combine(Path.Combine(Directory.GetCurrentDirectory(), Resources.GetMediaDirectory()), @"GameBoard\Initial.mp4")))
            {
                // Error
                Resources.Error(Resources.ErrorCode.MissingMedia, @"GameBoard\Initial.mp4");
            }
            else if (!File.Exists(Path.Combine(Path.Combine(Directory.GetCurrentDirectory(), Resources.GetMediaDirectory()), @"GameBoard\Rules.png")))
            {
                // Error
                Resources.Error(Resources.ErrorCode.MissingMedia, @"GameBoard\Rules.png");
            }
            else if (!File.Exists(Path.Combine(Path.Combine(Directory.GetCurrentDirectory(), Resources.GetMediaDirectory()), @"GameBoard\Title.png")))
            {
                // Error
                Resources.Error(Resources.ErrorCode.MissingMedia, @"GameBoard\Title.png");
            }
        }

        private void CheckRound()
        {
            // Check round
            switch (this.counter)
            {
                // Round 1 end
                case Resources.Round1:
                    // Add to round
                    this.round++;

                    // Display round 1
                    this.DisplaySingle(FormMediaSingle.MediaName.GameBoardRound0);

                    // Exit
                    break;

                // Round 2 end
                case Resources.Round2:
                    // Add to round
                    this.round++;

                    // Display round 2
                    this.DisplaySingle(FormMediaSingle.MediaName.GameBoardRound1);

                    // Exit
                    break;

                // Round 3 end
                case Resources.Round3:
                    // Add to round
                    this.round++;

                    // Display round 3
                    this.DisplaySingle(FormMediaSingle.MediaName.GameBoardRound2);

                    // Exit
                    break;

                // Final round end
                case Resources.RoundFinal:
                    // Display round final
                    this.DisplaySingle(FormMediaSingle.MediaName.GameBoardFinal);

                    // Setup finale
                    this.SetupFinale();

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

            // Load categories
            for (int i = 0; i < 10; i++)
            {
                // Set current information
                foreach (Control c in this.Controls)
                {
                    // Check if current control is picture box
                    if (c is PictureBox)
                    {
                        // Is the desired picture box
                        if (c.Name == "pictureBoxCategory" + i)
                        {
                            (c as PictureBox).Image = Image.FromFile(Path.Combine(Path.Combine(Directory.GetCurrentDirectory(), Resources.GetMediaDirectory()), @"GameBoard\Category" + i + ".png"));
                        }
                    }
                }
            }

            // Load other
            this.pictureBoxFinaleBackground.Image = Image.FromFile(Path.Combine(Path.Combine(Directory.GetCurrentDirectory(), Resources.GetMediaDirectory()), @"Finale\Background.png"));
            this.pictureBoxFinaleTitle.Image = Image.FromFile(Path.Combine(Path.Combine(Directory.GetCurrentDirectory(), Resources.GetMediaDirectory()), @"Finale\Title.png"));
            this.pictureBoxTitle.Image = Image.FromFile(Path.Combine(Path.Combine(Directory.GetCurrentDirectory(), Resources.GetMediaDirectory()), @"GameBoard\Title.png"));
        }

        private void LoadSettings()
        {
            // Variables
            var settings = ConfigurationManager.AppSettings;
            string[] tempColor = new string[1];

            // Attempt to read from settings
            try
            {
                // Check if settings exist
                if (settings.Count == 0)
                {
                    // No settings exist
                    Resources.Error(Resources.ErrorCode.NoAppSettings);
                }
                else
                {
                    // Settings: contestantNameX
                    // Set each contestant name
                    for (int i = 0; i < 3; i++)
                    {
                        // Check if empty
                        if (!String.IsNullOrEmpty(settings["contestantName" + i]))
                        {
                            // Set current information
                            foreach (Control c in this.Controls)
                            {
                                // Check if current control is button
                                if (c is Button)
                                {
                                    // Is the desired button
                                    if (c.Name == "buttonFinaleWinner" + i)
                                    {
                                        // Change text
                                        c.Text = settings["contestantName" + i];
                                    }
                                }
                            }
                        }
                        else
                        {
                            // Error
                            Resources.Error(Resources.ErrorCode.InvalidContestantName, "contestantName" + i);
                        }
                    }

                    // Settings: gameBoardColor
                    // Set the game board color for form and buttons

                    if (!String.IsNullOrEmpty(settings["gameBoardColor"]))
                    {
                        // Get color
                        tempColor = settings["gameBoardColor"].Split(' ');
                        if (tempColor.Length != 3)
                        {
                            // Error
                            Resources.Error(Resources.ErrorCode.InvalidGameBoardColor, settings["gameBoardColor"]);
                        }

                        // Set current information
                        this.BackColor = Color.FromArgb(Int32.Parse(tempColor[0]), Int32.Parse(tempColor[1]), Int32.Parse(tempColor[2]));

                        foreach (Control c in this.Controls)
                        {
                            // Check if current control is button
                            if (c is Button)
                            {
                                // Is the desired button
                                if (!c.Name.Contains("buttonFinaleWinner"))
                                {
                                    try
                                    {
                                        // Set color
                                        c.BackColor = Color.FromArgb(Int32.Parse(tempColor[0]), Int32.Parse(tempColor[1]), Int32.Parse(tempColor[2]));
                                        (c as Button).FlatAppearance.BorderColor = Color.FromArgb(Int32.Parse(tempColor[0]), Int32.Parse(tempColor[1]), Int32.Parse(tempColor[2]));
                                        (c as Button).FlatAppearance.CheckedBackColor = Color.FromArgb(Int32.Parse(tempColor[0]), Int32.Parse(tempColor[1]), Int32.Parse(tempColor[2]));
                                        (c as Button).FlatAppearance.MouseDownBackColor = Color.FromArgb(Int32.Parse(tempColor[0]), Int32.Parse(tempColor[1]), Int32.Parse(tempColor[2]));
                                        (c as Button).FlatAppearance.MouseOverBackColor = Color.FromArgb(Int32.Parse(tempColor[0]), Int32.Parse(tempColor[1]), Int32.Parse(tempColor[2]));
                                    }
                                    catch
                                    {
                                        // Error
                                        Resources.Error(Resources.ErrorCode.InvalidGameBoardColor, settings["gameBoardColor"]);
                                    }
                                }
                            }
                        }
                    }
                    else
                    {
                        // Error
                        Resources.Error(Resources.ErrorCode.InvalidGameBoardColor, settings["gameBoardColor"]);
                    }

                    // Settings: contestantColorX
                    // Set each contestant color
                    for (int i = 0; i < 3; i++)
                    {
                        // Check if empty
                        if (!String.IsNullOrEmpty(settings["contestantColor" + i]))
                        {
                            // Get color
                            tempColor = settings["contestantColor" + i].Split(' ');
                            if (tempColor.Length != 3)
                            {
                                // Error
                                Resources.Error(Resources.ErrorCode.InvalidContestantColor, "contestantColor" + i);
                            }

                            // Set current information
                            foreach (Control c in this.Controls)
                            {
                                // Check if current control is button
                                if (c is Button)
                                {
                                    // Is the desired button
                                    if (c.Name == "buttonFinaleWinner" + i)
                                    {
                                        try
                                        {
                                            // Set color
                                            c.ForeColor = Color.FromArgb(Int32.Parse(tempColor[0]), Int32.Parse(tempColor[1]), Int32.Parse(tempColor[2]));
                                        }
                                        catch
                                        {
                                            // Error
                                            Resources.Error(Resources.ErrorCode.InvalidContestantColor, "contestantColor" + i);
                                        }
                                    }
                                }
                            }
                        }
                        else
                        {
                            // Error
                            Resources.Error(Resources.ErrorCode.InvalidContestantColor, "contestantColor" + i);
                        }
                    }

                    // Settings: categoryColorX
                    // Check each category color
                    for (int i = 0; i < 10; i++)
                    {
                        // Check if empty
                        if (String.IsNullOrEmpty(settings["categoryColor" + i]))
                        {
                            // Error
                            Resources.Error(Resources.ErrorCode.InvalidCategoryColor, "categoryColor" + i);
                        }
                    }

                    // Set each category color
                    for (int i = 0; i < 10; i++)
                    {
                        // Get color
                        tempColor = settings["categoryColor" + i].Split(' ');
                        if (tempColor.Length != 3)
                        {
                            // Error
                            Resources.Error(Resources.ErrorCode.InvalidCategoryColor, "categoryColor" + i);
                        }

                        for (int j = 0; j < 12; j++)
                        {
                            // Set current information
                            foreach (Control c in this.Controls)
                            {
                                // Check if current control is button
                                if (c is Button)
                                {
                                    // Is the desired button
                                    if (c.Name == "buttonMain" + i + "_" + j)
                                    {
                                        try
                                        {
                                            // Set color
                                            c.ForeColor = Color.FromArgb(Int32.Parse(tempColor[0]), Int32.Parse(tempColor[1]), Int32.Parse(tempColor[2]));
                                        }
                                        catch
                                        {
                                            // Error
                                            Resources.Error(Resources.ErrorCode.InvalidCategoryColor, "categoryColor" + i);
                                        }
                                    }
                                }
                            }
                        }
                    }

                    // Settings: mediaTypeX_Y
                    // Check each media type
                    for (int i = 0; i < 10; i++)
                    {
                        for (int j = 0; j < 12; j++)
                        {
                            if (settings["mediaType" + i + "_" + j] != "ImageImage" &&
                                settings["mediaType" + i + "_" + j] != "ImageVideoImageImage" &&
                                settings["mediaType" + i + "_" + j] != "ImageVideoImageVideo" &&
                                settings["mediaType" + i + "_" + j] != "VideoImageImage" &&
                                settings["mediaType" + i + "_" + j] != "VideoImageVideo")
                            {
                                // Error
                                Resources.Error(Resources.ErrorCode.InvalidMediaType, "mediaType" + i + "_" + j);
                            }
                        }
                    }
                }
            }
            catch (ConfigurationErrorsException)
            {
                // Generic Error
                Resources.Error(Resources.ErrorCode.Generic);
            }
        }

        private void SetupFinale()
        {
            // Disable buttons
            foreach (Control c in this.Controls)
            {
                // Check if current control is button
                if (c is Button)
                {
                    // Is the desired button
                    if (c.Name.Contains("buttonMain"))
                    {
                        // Disable buttons
                        c.Enabled = false;
                        c.Visible = false;
                    }
                }
            }

            // Enable finale
            pictureBoxFinaleTitle.Enabled = true;
            pictureBoxFinaleTitle.Visible = true;

            pictureBoxFinaleBackground.Enabled = true;
            pictureBoxFinaleBackground.Visible = true;

            buttonFinaleWinner0.Enabled = true;
            buttonFinaleWinner0.Visible = true;
            buttonFinaleWinner0.BringToFront();

            buttonFinaleWinner1.Enabled = true;
            buttonFinaleWinner1.Visible = true;
            buttonFinaleWinner1.BringToFront();

            buttonFinaleWinner2.Enabled = true;
            buttonFinaleWinner2.Visible = true;
            buttonFinaleWinner2.BringToFront();

            buttonFinaleWinnerFinal.Enabled = true;
            buttonFinaleWinnerFinal.Visible = true;
            buttonFinaleWinnerFinal.BringToFront();
        }

        private void DisplayInitial()
        {
            // Variables
            Form tempForm = new FormMediaInitial();

            // Show form
            var result = tempForm.ShowDialog();
        }

        private void DisplaySingle(FormMediaSingle.MediaName mn)
        {
            // Variables
            Form tempForm = new FormMediaSingle(mn);

            // Show form
            var result = tempForm.ShowDialog();
        }

        private void DisplayMedia(int cat, int num, FormMediaMain.MediaType mt)
        {
            // Variables
            Form tempForm = new FormMediaMain(cat, num, mt);

            // Show form
            var result = tempForm.ShowDialog();
        }

        private void DisplayScoreAdd()
        {
            // Variables
            Form tempForm = new FormScoreAdd(this);

            // Show form
            var result = tempForm.ShowDialog();
        }

        private void DisplayScoreView()
        {
            // Variables
            Form tempForm = new FormScoreView(this);

            // Show form
            var result = tempForm.ShowDialog();
        }

        private void DisplayEdit()
        {
            // Variables
            Form tempForm = new FormScoreEdit(this);

            // Show form
            var result = tempForm.ShowDialog();
        }

        private void DisplayMedia()
        {
            // Variables
            Form tempForm = new FormMediaCustom();

            // Show form
            var result = tempForm.ShowDialog();
        }

        private void DisplayInfo()
        {
            // Variables
            Form tempForm = new FormInfoMain();

            // Show form
            var result = tempForm.ShowDialog();
        }

        private void DefaultLog()
        {
            // Variables
            Configuration config;

            // Open manager
            config = ConfigurationManager.OpenExeConfiguration(ConfigurationUserLevel.None);

            // Set original log
            this.logOriginal = config.AppSettings.Settings["gameplayLog"].Value;

            // Set default media log
            for (int i = 0; i < 10; i++)
            {
                for (int j = 0; j < 12; j++)
                {
                    // Set default value
                    this.logMedia[i, j] = false;
                }
            }
        }

        public void UpdateLog()
        {
            // Variables
            string dataMain, dataMedia;
            var settings = ConfigurationManager.AppSettings;
            Configuration config;

            // Open manager
            config = ConfigurationManager.OpenExeConfiguration(ConfigurationUserLevel.None);

            // Set data main
            dataMain = "\r\n\r\n\r\n\r\nGame (" + DateTime.Now.ToString("ddd MMM d yyyy HH: mm") + ")\r\n\r\n" + settings["contestantName0"] + ": " + this.score0 + "\r\n" + settings["contestantName1"] + ": " + this.score1 + "\r\n" + settings["contestantName2"] + ": " + this.score2 + "\r\nCounter: " + this.counter + "\r\nRound Number: " + this.round + "\r\n\r\nMedia Opened:";
            dataMedia = "";

            // Set data media
            for (int i = 0; i < 10; i++)
            {
                for (int j = 0; j < 12; j++)
                {
                    // Check value
                    if(this.logMedia[i, j])
                    {
                        // Add to string
                        dataMedia += "\r\n" + "Media " + (i + 1) + " " + (j + 1);
                    }
                }
            }

            // Set value
            config.AppSettings.Settings["gameplayLog"].Value = this.logOriginal + dataMain + dataMedia;

            // Save configuration
            config.Save(ConfigurationSaveMode.Full, true);
            ConfigurationManager.RefreshSection("appSettings");
        }
    }
}
