/********************************
 * Custom Game Show
 * FormMediaMain.Designer.cs
 * Created by Justin Leonard
********************************/

namespace CustomGameShow
{
    partial class FormMediaMain
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
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(FormMediaMain));
            this.pictureBoxImage = new System.Windows.Forms.PictureBox();
            this.WindowsMediaPlayerMain = new AxWMPLib.AxWindowsMediaPlayer();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBoxImage)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.WindowsMediaPlayerMain)).BeginInit();
            this.SuspendLayout();
            // 
            // pictureBoxImage
            // 
            this.pictureBoxImage.BackColor = System.Drawing.Color.Transparent;
            this.pictureBoxImage.Enabled = false;
            this.pictureBoxImage.Location = new System.Drawing.Point(0, 0);
            this.pictureBoxImage.Name = "pictureBoxImage";
            this.pictureBoxImage.Size = new System.Drawing.Size(1920, 1080);
            this.pictureBoxImage.TabIndex = 0;
            this.pictureBoxImage.TabStop = false;
            this.pictureBoxImage.Visible = false;
            this.pictureBoxImage.Click += new System.EventHandler(this.pictureBoxImage_Click);
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
            this.WindowsMediaPlayerMain.Visible = false;
            this.WindowsMediaPlayerMain.PlayStateChange += new AxWMPLib._WMPOCXEvents_PlayStateChangeEventHandler(this.WindowsMediaPlayerMain_PlayStateChange);
            // 
            // FormMediaMain
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1920, 1080);
            this.Controls.Add(this.WindowsMediaPlayerMain);
            this.Controls.Add(this.pictureBoxImage);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.None;
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.KeyPreview = true;
            this.MaximizeBox = false;
            this.MinimizeBox = false;
            this.Name = "FormMediaMain";
            this.SizeGripStyle = System.Windows.Forms.SizeGripStyle.Hide;
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "Custom Game Show";
            this.FormClosing += new System.Windows.Forms.FormClosingEventHandler(this.FormMediaMain_FormClosing);
            this.KeyDown += new System.Windows.Forms.KeyEventHandler(this.FormMediaMain_KeyDown);
            ((System.ComponentModel.ISupportInitialize)(this.pictureBoxImage)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.WindowsMediaPlayerMain)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.PictureBox pictureBoxImage;
        private AxWMPLib.AxWindowsMediaPlayer WindowsMediaPlayerMain;
    }
}