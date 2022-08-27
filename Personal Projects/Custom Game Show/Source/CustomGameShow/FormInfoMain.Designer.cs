/********************************
 * Custom Game Show
 * FormInfoMain.Designer.cs
 * Created by Justin Leonard
********************************/

namespace CustomGameShow
{
    partial class FormInfoMain
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
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(FormInfoMain));
            this.buttonExit = new System.Windows.Forms.Button();
            this.buttonMedia = new System.Windows.Forms.Button();
            this.buttonCustom = new System.Windows.Forms.Button();
            this.buttonRules = new System.Windows.Forms.Button();
            this.labelTitle = new System.Windows.Forms.Label();
            this.SuspendLayout();
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
            this.buttonExit.Location = new System.Drawing.Point(91, 469);
            this.buttonExit.Name = "buttonExit";
            this.buttonExit.Size = new System.Drawing.Size(468, 75);
            this.buttonExit.TabIndex = 0;
            this.buttonExit.TabStop = false;
            this.buttonExit.Text = "Exit";
            this.buttonExit.UseVisualStyleBackColor = false;
            this.buttonExit.Click += new System.EventHandler(this.buttonExit_Click);
            // 
            // buttonMedia
            // 
            this.buttonMedia.BackColor = System.Drawing.SystemColors.ScrollBar;
            this.buttonMedia.BackgroundImage = ((System.Drawing.Image)(resources.GetObject("buttonMedia.BackgroundImage")));
            this.buttonMedia.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.buttonMedia.Cursor = System.Windows.Forms.Cursors.Hand;
            this.buttonMedia.FlatAppearance.BorderColor = System.Drawing.SystemColors.ScrollBar;
            this.buttonMedia.FlatAppearance.BorderSize = 0;
            this.buttonMedia.FlatAppearance.CheckedBackColor = System.Drawing.SystemColors.ScrollBar;
            this.buttonMedia.FlatAppearance.MouseDownBackColor = System.Drawing.SystemColors.ScrollBar;
            this.buttonMedia.FlatAppearance.MouseOverBackColor = System.Drawing.SystemColors.ScrollBar;
            this.buttonMedia.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.buttonMedia.Font = new System.Drawing.Font("Arial", 36F, System.Drawing.FontStyle.Bold);
            this.buttonMedia.Location = new System.Drawing.Point(91, 259);
            this.buttonMedia.Name = "buttonMedia";
            this.buttonMedia.Size = new System.Drawing.Size(468, 75);
            this.buttonMedia.TabIndex = 0;
            this.buttonMedia.TabStop = false;
            this.buttonMedia.Text = "Media";
            this.buttonMedia.UseVisualStyleBackColor = false;
            this.buttonMedia.Click += new System.EventHandler(this.buttonMedia_Click);
            // 
            // buttonCustom
            // 
            this.buttonCustom.BackColor = System.Drawing.SystemColors.ScrollBar;
            this.buttonCustom.BackgroundImage = ((System.Drawing.Image)(resources.GetObject("buttonCustom.BackgroundImage")));
            this.buttonCustom.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.buttonCustom.Cursor = System.Windows.Forms.Cursors.Hand;
            this.buttonCustom.FlatAppearance.BorderColor = System.Drawing.SystemColors.ScrollBar;
            this.buttonCustom.FlatAppearance.BorderSize = 0;
            this.buttonCustom.FlatAppearance.CheckedBackColor = System.Drawing.SystemColors.ScrollBar;
            this.buttonCustom.FlatAppearance.MouseDownBackColor = System.Drawing.SystemColors.ScrollBar;
            this.buttonCustom.FlatAppearance.MouseOverBackColor = System.Drawing.SystemColors.ScrollBar;
            this.buttonCustom.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.buttonCustom.Font = new System.Drawing.Font("Arial", 36F, System.Drawing.FontStyle.Bold);
            this.buttonCustom.Location = new System.Drawing.Point(91, 364);
            this.buttonCustom.Name = "buttonCustom";
            this.buttonCustom.Size = new System.Drawing.Size(468, 75);
            this.buttonCustom.TabIndex = 0;
            this.buttonCustom.TabStop = false;
            this.buttonCustom.Text = "Custom";
            this.buttonCustom.UseVisualStyleBackColor = false;
            this.buttonCustom.Click += new System.EventHandler(this.buttonCustom_Click);
            // 
            // buttonRules
            // 
            this.buttonRules.BackColor = System.Drawing.SystemColors.ScrollBar;
            this.buttonRules.BackgroundImage = ((System.Drawing.Image)(resources.GetObject("buttonRules.BackgroundImage")));
            this.buttonRules.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.buttonRules.Cursor = System.Windows.Forms.Cursors.Hand;
            this.buttonRules.FlatAppearance.BorderColor = System.Drawing.SystemColors.ScrollBar;
            this.buttonRules.FlatAppearance.BorderSize = 0;
            this.buttonRules.FlatAppearance.CheckedBackColor = System.Drawing.SystemColors.ScrollBar;
            this.buttonRules.FlatAppearance.MouseDownBackColor = System.Drawing.SystemColors.ScrollBar;
            this.buttonRules.FlatAppearance.MouseOverBackColor = System.Drawing.SystemColors.ScrollBar;
            this.buttonRules.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.buttonRules.Font = new System.Drawing.Font("Arial", 36F, System.Drawing.FontStyle.Bold);
            this.buttonRules.Location = new System.Drawing.Point(91, 153);
            this.buttonRules.Name = "buttonRules";
            this.buttonRules.Size = new System.Drawing.Size(468, 75);
            this.buttonRules.TabIndex = 0;
            this.buttonRules.TabStop = false;
            this.buttonRules.Text = "Rules";
            this.buttonRules.UseVisualStyleBackColor = false;
            this.buttonRules.Click += new System.EventHandler(this.buttonRules_Click);
            // 
            // labelTitle
            // 
            this.labelTitle.AutoSize = true;
            this.labelTitle.Font = new System.Drawing.Font("Arial Black", 48F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.labelTitle.ForeColor = System.Drawing.SystemColors.ControlText;
            this.labelTitle.Location = new System.Drawing.Point(106, 30);
            this.labelTitle.Name = "labelTitle";
            this.labelTitle.Size = new System.Drawing.Size(445, 90);
            this.labelTitle.TabIndex = 0;
            this.labelTitle.Text = "Information";
            // 
            // FormInfoMain
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.SystemColors.ScrollBar;
            this.ClientSize = new System.Drawing.Size(650, 572);
            this.Controls.Add(this.buttonExit);
            this.Controls.Add(this.buttonMedia);
            this.Controls.Add(this.buttonCustom);
            this.Controls.Add(this.buttonRules);
            this.Controls.Add(this.labelTitle);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.None;
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.KeyPreview = true;
            this.MaximizeBox = false;
            this.MinimizeBox = false;
            this.Name = "FormInfoMain";
            this.SizeGripStyle = System.Windows.Forms.SizeGripStyle.Hide;
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "Custom Game Show";
            this.KeyDown += new System.Windows.Forms.KeyEventHandler(this.FormInfoMain_KeyDown);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button buttonExit;
        private System.Windows.Forms.Button buttonMedia;
        private System.Windows.Forms.Button buttonCustom;
        private System.Windows.Forms.Button buttonRules;
        private System.Windows.Forms.Label labelTitle;
    }
}