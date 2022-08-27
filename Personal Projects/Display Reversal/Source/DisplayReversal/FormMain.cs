/********************************
 * Display Reversal
 * FormMain.cs
 * Created by Justin Leonard
********************************/

using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Diagnostics;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace DisplayReversal
{
    public partial class FormMain : Form
    {
        /*
         * Fields
         */
        public const string DeviceTV = @"\\.\DISPLAY1";
        public const string DeviceMonitor = @"\\.\DISPLAY2";

        /*
         * Constructor
         */
        
        public FormMain()
        {
            // Initialize
            InitializeComponent();
        }

        /*
         * Form Events
         */
        
        private void FormMain_Load(object sender, EventArgs e)
        {
            // Check nircmd
            this.CheckNircmd();

            // Reverse display
            this.ReverseDefaultDisplay();
        }

        /*
         * Methods
         */
        
        public void CheckNircmd()
        {
            // Check if nircmd is in the same directory as application
            if (!File.Exists(Path.Combine(AppDomain.CurrentDomain.BaseDirectory, "nircmd.exe")))
            {
                // Show error
                MessageBox.Show("nircmd.exe is not in the application folder", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);

                // Close application
                this.Close();
            }
        }

        public void ReverseDefaultDisplay()
        {
            // Variables
            string newDisplay = String.Empty;

            // Check primary screen
            if (Screen.PrimaryScreen.DeviceName == DeviceTV)
            {
                // Set new display
                newDisplay = DeviceMonitor;
            }
            else if (Screen.PrimaryScreen.DeviceName == DeviceMonitor)
            {
                // Set new display
                newDisplay = DeviceTV;
            }

            // Create cmd process
            Process cmd = new Process();
            cmd.StartInfo.FileName = "cmd.exe";
            cmd.StartInfo.RedirectStandardInput = true;
            cmd.StartInfo.RedirectStandardOutput = true;
            cmd.StartInfo.CreateNoWindow = true;
            cmd.StartInfo.UseShellExecute = false;
            cmd.Start();

            // Run command
            cmd.StandardInput.WriteLine("nircmd.exe setprimarydisplay " + newDisplay);
            cmd.StandardInput.Flush();
            cmd.StandardInput.Close();
            cmd.WaitForExit();

            // Close application
            this.Close();
        }
    }
}
