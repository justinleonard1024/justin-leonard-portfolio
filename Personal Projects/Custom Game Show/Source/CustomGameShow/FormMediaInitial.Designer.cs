/********************************
 * Custom Game Show
 * FormMediaInitial.Designer.cs
 * Created by Justin Leonard
********************************/

namespace CustomGameShow
{
    partial class FormMediaInitial
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(FormMediaInitial));
            this.WindowsMediaPlayerMain = new AxWMPLib.AxWindowsMediaPlayer();
            ((System.ComponentModel.ISupportInitialize)(this.WindowsMediaPlayerMain)).BeginInit();
            this.SuspendLayout();
            // 
            // WindowsMediaPlayerMain
            // 
            this.WindowsMediaPlayerMain.Enabled = true;
            this.WindowsMediaPlayerMain.Location = new System.Drawing.Point(0, 0);
            this.WindowsMediaPlayerMain.Name = "WindowsMediaPlayerMain";
            this.WindowsMediaPlayerMain.OcxState = ((System.Windows.Forms.AxHost.State)(resources.GetObject("WindowsMediaPlayerMain.OcxState")));
            this.WindowsMediaPlayerMain.Size = new System.Drawing.Size(1920, 1080);
            this.WindowsMediaPlayerMain.TabIndex = 0;
            this.WindowsMediaPlayerMain.TabStop = false;
            this.WindowsMediaPlayerMain.PlayStateChange += new AxWMPLib._WMPOCXEvents_PlayStateChangeEventHandler(this.WindowsMediaPlayerMain_PlayStateChange);
            // 
            // FormMediaInitial
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1920, 1080);
            this.Controls.Add(this.WindowsMediaPlayerMain);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.None;
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.KeyPreview = true;
            this.MaximizeBox = false;
            this.MinimizeBox = false;
            this.Name = "FormMediaInitial";
            this.SizeGripStyle = System.Windows.Forms.SizeGripStyle.Hide;
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "Custom Game Show";
            this.FormClosing += new System.Windows.Forms.FormClosingEventHandler(this.FormMediaInitial_FormClosing);
            this.Load += new System.EventHandler(this.FormMediaInitial_Load);
            this.KeyDown += new System.Windows.Forms.KeyEventHandler(this.FormMediaInitial_KeyDown);
            ((System.ComponentModel.ISupportInitialize)(this.WindowsMediaPlayerMain)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        private AxWMPLib.AxWindowsMediaPlayer WindowsMediaPlayerMain;
    }
}