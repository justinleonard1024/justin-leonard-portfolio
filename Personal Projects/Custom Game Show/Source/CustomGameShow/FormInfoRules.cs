/********************************
 * Custom Game Show
 * FormInfoRules.cs
 * Created by Justin Leonard
********************************/

using System;
using System.Drawing;
using System.IO;
using System.Windows.Forms;

namespace CustomGameShow
{
    public partial class FormInfoRules : Form
    {
        /*
         * Constructor
         */
        
        public FormInfoRules()
        {
            // Initialize
            InitializeComponent();

            // Load media
            this.LoadMedia();
        }

        /*
         * Form Events
         */
        
        private void FormInfoRules_KeyDown(object sender, KeyEventArgs e)
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
        
        private void buttonExit_Click(object sender, EventArgs e)
        {
            // Exit form
            this.Close();
        }

        /*
         * Methods
         */
        
        private void LoadMedia()
        {
            // Check files exist
            if (!File.Exists(Path.Combine(Path.Combine(Directory.GetCurrentDirectory(), Resources.GetMediaDirectory()), @"GameBoard\Rules.png")))
            {
                // Error
                Resources.Error(Resources.ErrorCode.MissingMedia, @"GameBoard\Rules.png");
            }

            // Load media
            this.pictureBoxRules.Image = Image.FromFile(Path.Combine(Path.Combine(Directory.GetCurrentDirectory(), Resources.GetMediaDirectory()), @"GameBoard\Rules.png"));
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
