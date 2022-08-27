/********************************
 * Custom Game Show
 * FormInfoRules.Designer.cs
 * Created by Justin Leonard
********************************/

namespace CustomGameShow
{
    partial class FormInfoRules
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
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(FormInfoRules));
            this.labelTitle = new System.Windows.Forms.Label();
            this.buttonExit = new System.Windows.Forms.Button();
            this.pictureBoxRules = new System.Windows.Forms.PictureBox();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBoxRules)).BeginInit();
            this.SuspendLayout();
            // 
            // labelTitle
            // 
            this.labelTitle.AutoSize = true;
            this.labelTitle.Font = new System.Drawing.Font("Arial Black", 72F, System.Drawing.FontStyle.Bold);
            this.labelTitle.ForeColor = System.Drawing.SystemColors.ControlText;
            this.labelTitle.Location = new System.Drawing.Point(792, 3);
            this.labelTitle.Name = "labelTitle";
            this.labelTitle.Size = new System.Drawing.Size(349, 136);
            this.labelTitle.TabIndex = 0;
            this.labelTitle.Text = "Rules";
            // 
            // buttonExit
            // 
            this.buttonExit.BackColor = System.Drawing.SystemColors.ScrollBar;
            this.buttonExit.BackgroundImage = ((System.Drawing.Image)(resources.GetObject("buttonExit.BackgroundImage")));
            this.buttonExit.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.buttonExit.Cursor = System.Windows.Forms.Cursors.Hand;
            this.buttonExit.FlatAppearance.BorderColor = System.Drawing.SystemColors.ScrollBar;
            this.buttonExit.FlatAppearance.BorderSize = 0;
            this.buttonExit.FlatAppearance.CheckedBackColor = System.Drawing.SystemColors.ScrollBar;
            this.buttonExit.FlatAppearance.MouseDownBackColor = System.Drawing.SystemColors.ScrollBar;
            this.buttonExit.FlatAppearance.MouseOverBackColor = System.Drawing.SystemColors.ScrollBar;
            this.buttonExit.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.buttonExit.Font = new System.Drawing.Font("Arial", 36F, System.Drawing.FontStyle.Bold);
            this.buttonExit.Location = new System.Drawing.Point(726, 961);
            this.buttonExit.Name = "buttonExit";
            this.buttonExit.Size = new System.Drawing.Size(468, 75);
            this.buttonExit.TabIndex = 0;
            this.buttonExit.TabStop = false;
            this.buttonExit.Text = "Exit";
            this.buttonExit.UseVisualStyleBackColor = false;
            this.buttonExit.Click += new System.EventHandler(this.buttonExit_Click);
            // 
            // pictureBoxRules
            // 
            this.pictureBoxRules.BackColor = System.Drawing.Color.Transparent;
            this.pictureBoxRules.Location = new System.Drawing.Point(12, 160);
            this.pictureBoxRules.Name = "pictureBoxRules";
            this.pictureBoxRules.Size = new System.Drawing.Size(1896, 758);
            this.pictureBoxRules.TabIndex = 0;
            this.pictureBoxRules.TabStop = false;
            // 
            // FormInfoRules
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.SystemColors.ScrollBar;
            this.ClientSize = new System.Drawing.Size(1920, 1080);
            this.Controls.Add(this.pictureBoxRules);
            this.Controls.Add(this.buttonExit);
            this.Controls.Add(this.labelTitle);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.None;
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.KeyPreview = true;
            this.MaximizeBox = false;
            this.MinimizeBox = false;
            this.Name = "FormInfoRules";
            this.SizeGripStyle = System.Windows.Forms.SizeGripStyle.Hide;
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "Custom Game Show";
            this.KeyDown += new System.Windows.Forms.KeyEventHandler(this.FormInfoRules_KeyDown);
            ((System.ComponentModel.ISupportInitialize)(this.pictureBoxRules)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label labelTitle;
        private System.Windows.Forms.Button buttonExit;
        private System.Windows.Forms.PictureBox pictureBoxRules;
    }
}